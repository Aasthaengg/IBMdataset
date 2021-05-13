n, m = map(int, input().split())

INF = 10**10

# Warshall-Floyd
dist = [[INF for _ in range(n)] for _ in range(n)]
edge = []
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    dist[a][b] = c
    dist[b][a] = c
    edge.append([a, b, c])

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

ans = m
for e in edge:
    flag = False
    i, j, c = e
    for s in range(n):
        if flag:
            break
        for t in range(n):
            if dist[s][i]+c+dist[j][t] == dist[s][t]:
                flag = True
                break
    if flag:
        ans -= 1
print(ans)