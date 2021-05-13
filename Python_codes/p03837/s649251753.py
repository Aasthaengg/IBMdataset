from scipy.sparse.csgraph import dijkstra as di

n,m = map(int, input().split())
edges = []
grid = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    grid[a][b] = grid[b][a] = c
    edges.append((a,b,c))

g = di(grid)
ans = 0
for a,b,c in edges:
    if g[a][b] < c:
        ans += 1
print(ans)
