import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

#-1:undefined 0:unkind 1:honest
honest_thought = [[] for _ in range(n+1)] 
unkind_thought = [[] for _ in range(n+1)] 

for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = list(map(int, input().split()))
        if y == 0:
            unkind_thought[i].append(x)
        else:
            honest_thought[i].append(x)


ans = 0

for i in range(2 ** n):
    #print(i)
    flag = True

    #最初を設定
    honest = [False] * (n+1)
    unkind = [False] * (n+1)

    q = deque()
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            honest[j+1] = True
            q.append(j)

    while len(q) > 0 and flag:
        v = q.popleft()
        for x in unkind_thought[v]:
            if honest[x]:
                flag = False
                break
            elif not unkind[x]:
                unkind[x] = True
        for x in honest_thought[v]:
            if unkind[x]:
                flag = False
                break
            elif not honest[x]:
                flag = False
                break

    if flag:
        ans = max(ans, honest.count(True))


print(ans)
    

