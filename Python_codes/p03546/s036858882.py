H, W = map(int,input().split())
N = 10
cost = [[0] * N for _ in range(N)]
for i in range(N):
    for j, c in enumerate(map(int, input().split())):
        cost[i][j] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

ans = 0
for _ in range(H):
    for x in map(int, input().split()):
        if x >= 0:
            ans += cost[x][1]
print(ans)