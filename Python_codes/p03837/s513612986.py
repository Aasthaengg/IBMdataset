N, M = map(int, input().split(' '))
dist = [[10 ** 9 for _ in range(N)] for _ in range(N)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split(' '))
    dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c)
    dist[b - 1][a - 1] = min(dist[b - 1][a - 1], c)
    edges.append((a - 1, b - 1, c))

for k in range(N):
    dist[k][k] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for (u, v, cost) in edges:
    flag = False
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            flag |= ((dist[i][u] + cost + dist[v][j]) == dist[i][j])
    ans += 1 - int(flag)
print(ans)