import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7
INF = 10 ** 18

N, M, P = map(int, input().split())
G = []
G_append = G.append

g = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G_append((A, B, -C + P))
    g[A].append(B)

d = [INF] * (N + 1) #最短距離を記録しておくリスト
d[1] = 0
def find_negative_loop1(): #負の閉路が存在するかを確認
    for i in range(N):
        for j in range(M): #無向グラフのときは辺は実質的には2倍
            e = G[j]
            if d[e[0]] != INF and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                #頂点の回数と同じだけループを回しても更新が起きる-->負の閉回路が存在
                if i == N-1:
                    return True #Trueの時, 負の閉路が存在
    return False #Falseの時, 負の閉路が存在しない

def find_negative_loop2(): #負の閉路が存在するかを確認
    check = [False] * (N + 1)
    for _ in range(N):
        for j in range(M): #無向グラフのときは辺は実質的には2倍
            e = G[j]
            if d[e[0]] != INF and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                check[e[1]] = True
            if check[e[0]]:
                check[e[1]] = True
    return check[N]

#呼び出しスタート地点を入れる
if find_negative_loop1():
    if find_negative_loop2():
        print (-1)
    else:
        print (max(0, -d[N]))
else:
    print (max(0, -d[N]))



