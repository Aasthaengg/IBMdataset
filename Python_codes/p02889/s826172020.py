N, M, L= map(int,input().split())
cost = [[float('inf')]*N for i in range(N)]

for i in range(N):
    cost[i][i] = 0

for _ in range(M):
    a,b,c = map(int,input().split())
    cost[a-1][b-1] = c
    cost[b-1][a-1] = c
def func(f):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                f[i][j] = min(f[i][k] + f[k][j], f[i][j])
    return f
cost = func(cost)
for i in range(N):
    for j in range(N):
        if cost[i][j] > L:
            cost[i][j] = float('inf')
        else:
            cost[i][j] = 1
cost = func(cost)

Q = int(input())
ans = []
for i in range(Q):
    s,t = map(int,input().split())
    ans.append(cost[s-1][t-1]-1)
for i in ans:
    if i == float('inf'):
        print(-1)
    else:
        print(i)
