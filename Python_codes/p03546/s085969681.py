H, W = map(int,input().split())
cost = [list(map(int,input().split())) for _ in range(10)]
A = [list(map(int,input().split())) for _ in range(H)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

ans = 0
for h in range(H):
    for w in range(W):
        if A[h][w] != -1:
            ans += cost[A[h][w]][1]
print(ans)