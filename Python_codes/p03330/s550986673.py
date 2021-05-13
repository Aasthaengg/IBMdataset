N, C = map(int, input().split())
D = [list(map(int, input().split())) for i in range(C)]
G = [list(map(int, input().split())) for i in range(N)]

cost = [[0 for j in range(C)] for i in range(3)]
for i in range(N):
    for j in range(N):
        rem = (i+j+2)%3
        x = G[i][j] -1
        for y in range(C):
            cost[rem][y] += D[x][y]
ans = float('inf')
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if i == k or j == k:
                continue
            ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
print(ans)