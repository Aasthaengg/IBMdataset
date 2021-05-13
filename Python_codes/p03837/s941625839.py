from copy import deepcopy
INF = 1 << 32
n, m = map(int, input().split())
d = [[INF] * n for i in range(n)]
# 入力
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    d[a][b] = c
    d[b][a] = c # 無向グラフ
for i in range(n):
    d[i][i] = 0

dist = deepcopy(d)
# FloydWarshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if d[i][j] < INF and d[i][j] != dist[i][j]:
            cnt += 1
print(cnt)