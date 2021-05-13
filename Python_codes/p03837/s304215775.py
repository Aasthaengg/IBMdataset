import sys
input = sys.stdin.buffer.readline
N, M = map(int, input().split())
d = [[float("inf")] * (N + 1) for _ in range(N + 1)]
e = [[0] * (N + 1) for _ in range(N + 1)]
prev = [[-1] * (N + 1) for _ in range(N + 1)]
res = 2 * M
for _ in range(M):
  a, b, c = map(int, input().split())
  d[a][b] = c
  d[b][a] = c
for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      if d[i][j] > d[i][k] + d[k][j]:
        d[i][j] = d[i][k] + d[k][j]
        if prev[k][j] == -1:
          prev[i][j] = k
        else:
          prev[i][j] = prev[k][j]
for i in range(1, N):
  for j in range(i + 1, N + 1):
    s = i
    t = j
    while prev[s][t] != -1:
      p = prev[s][t]
      e[p][t] = 1
      e[t][p] = 1
      t = p
    e[s][t] = 1
    e[t][s] = 1
for i in range(1, N + 1):
  res -= sum(e[i])
print(res // 2)