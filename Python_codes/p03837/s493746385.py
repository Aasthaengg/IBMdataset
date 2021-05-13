n, m = map(lambda x: int(x), input().split())
a = [0] * m
b = [0] * m
c = [0] * m
for i in range(m):
    a[i], b[i], c[i] = map(lambda x: int(x), input().split())

inf = 100 * 1000
dist = [[inf for i in range(n+1)] for j in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0
for i in range(m):
    dist[a[i]][b[i]] = c[i]
    dist[b[i]][a[i]] = c[i]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

count = 0
for i in range(m):
    if dist[a[i]][b[i]] < c[i]:
        count += 1
print(count)