n, m = map(int, input().split())
inf = float("inf")
edges = [[inf]*n for _ in range(n)]
path = [[inf]*n for _ in range(n)]
edges_list = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a][b] = c
    edges[b][a] = c
    path[a][b] = c
    path[b][a] = c
    edges_list.append((a, b))

for i in range(n):
    path[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            path[i][j] = min(path[i][j], path[i][k] + path[k][j])

count = 0
for a, b in edges_list:
    if path[a][b] < edges[a][b]:
        count += 1

print(count)