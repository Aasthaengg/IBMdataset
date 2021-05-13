# ABC143-E

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,M,L = MI()

inf = 10**12
cost = [[inf]*(N+1) for _ in range(N+1)]  # cost[i][j] = 町iから町jへ移動するのにかかる燃料の総和

# WarshallFloyd法

for i in range(M):
    a,b,c = MI()
    cost[a][b] = c
    cost[b][a] = c

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])

ans = [[inf]*(N+1) for _ in range(N+1)]  # ans[i][j] = 町iから町jへ移動するために必要な燃料補給の回数+1

# WarshallFloyd法、再び

for i in range(N+1):
    for j in range(N+1):
        if cost[i][j] <= L:
            ans[i][j] = 1

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            ans[i][j] = min(ans[i][j],ans[i][k]+ans[k][j])

Q = I()
for i in range(Q):
    s,t = MI()
    if ans[s][t] == inf:
        print(-1)
        continue
    print(ans[s][t]-1)
