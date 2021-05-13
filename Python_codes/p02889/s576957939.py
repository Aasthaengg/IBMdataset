n, m, l = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]

INF = 1001001001
dist = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for road in ls:
    dist[road[0]-1][road[1]-1] = dist[road[1]-1][road[0]-1] = road[2]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

dist2 = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dist[i][j] <= l:
            dist2[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist2[i][j] = min(dist2[i][j], dist2[i][k] + dist2[k][j])

for el in query:
    ans = dist2[el[0]-1][el[1]-1]-1
    if dist2[el[0]-1][el[1]-1] == INF:
        ans = -1
    print(ans)