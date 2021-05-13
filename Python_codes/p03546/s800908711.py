H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
grid = [list(map(int, input().split())) for _ in range(H)]

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n = 10
d = [[float("inf")]*n for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for x in range(n):
    for y in range(n):
        d[x][y] = c[x][y]
        d[y][x] = c[y][x]
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
cost = warshall_floyd(d)
ans = 0
for h in range(H):
    for w in range(W):
        if grid[h][w] != -1:
            ans += cost[grid[h][w]][1]
print(ans)