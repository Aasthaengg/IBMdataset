from itertools import permutations

n, m, r = map(int, input().split())
city = list(map(int, input().split()))
for i in range(r):
    city[i] -= 1
to = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    to[a].append([b, c])
    to[b].append([a, c])

INF = 10**15
dist = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
    for j in range(len(to[i])):
        dist[i][to[i][j][0]] = to[i][j][1]
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

ans = INF
for v in permutations(city):
    tmp = 0
    for i in range(r-1):
        tmp += dist[v[i]][v[i+1]]
    ans = min(ans, tmp)

print(ans)