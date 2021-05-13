INFTY = 10**4+10
H,W = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(10)]
cost = [[INFTY for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        cost[i][j] = C[i][j]
for k in range(10):
    for i in range(10):
        for j in range(10):
            cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])
A = [list(map(int,input().split())) for _ in range(H)]
tot = 0
for i in range(H):
    for j in range(W):
        if A[i][j]==1 or A[i][j]==-1:continue
        tot += cost[A[i][j]][1]
print(tot)