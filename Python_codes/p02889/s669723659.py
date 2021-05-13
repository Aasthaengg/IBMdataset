import sys
input = sys.stdin.readline
N, M, L = map(int, input().split())
d = [[10 ** 16 * (i != j) for j in range(N + 1)] for i in range(N + 1)]
for _ in range(M):
  x, y, c = map(int, input().split())
  d[x][y] = c
  d[y][x] = c
for k in range(N + 1):
  for i in range(N + 1):
    for j in range(N + 1): d[i][j] = min(d[i][j], d[i][k] + d[k][j])

dd = [[(d[i][j] <= L) + (d[i][j] > L) * 10 ** 16 for j in range(N + 1)] for i in range(N + 1)]
for k in range(N + 1):
  for i in range(N + 1):
    for j in range(N + 1): dd[i][j] = min(dd[i][j], dd[i][k] + dd[k][j])

for _ in range(int(input())):
  s, t = map(int, input().split())
  if dd[s][t] != 10 ** 16: print(dd[s][t] - 1)
  else: print(-1)