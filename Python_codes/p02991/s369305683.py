#行けるかどうかは判断できる、回数は判断できない
#-->回数を数えるように変更
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

#辺の管理(1-index)s
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u] += [v]
# print (edge)
INF = 10 ** 9
used1 = [INF] * (N + 1) #1手目で行けたところ
used2 = [INF] * (N + 1) #2手目で行けたところ
used3 = [INF] * (N + 1) #3手目で行けたところ

def solve(s): #スタート地点s
    from collections import deque
    used3[s] = 0
    
    #ここまで最初の準備
    from1 = deque() #used1から向かう辺のdeque
    from2 = deque() #used2から向かう辺のdeque
    from3 = deque() #used3から向かう辺のdeque

    f1append = from1.append
    f2append = from2.append
    f3append = from3.append

    f1pop = from1.popleft
    f2pop = from2.popleft
    f3pop = from3.popleft

    for i in edge[s]:
        # print (i)
        f3append(i)

    #deque: 空のとき = False
    count = 0
    while from1 or from2 or from3: #どれかが空ではないとき
        count += 1
        #from3 --> from1 -->from2の順にすべて処理
        for _ in range(len(from3)):
            # print ('from3', count)
            v = f3pop()
            if used1[v] == INF:
                used1[v] = count
                for i in edge[v]:
                    f1append(i)
        
        for _ in range(len(from1)): #中にある分すべてを処理する
            # print ('from1', count)
            v = f1pop()
            if used2[v] == INF:
                used2[v] = count
                for i in edge[v]:
                    f2append(i)
        
        for _ in range(len(from2)):
            # print ('from2', count)
            v = f2pop()
            if used3[v] == INF:
                used3[v] = count
                for i in edge[v]:
                    f3append(i)
        
    return


S, T = map(int, input().split())

solve(S)
# print (1, used1)
# print (2, used2)
# print (3, used3)

if used3[T] == INF:
    print (-1)
else:
    print (used3[T])