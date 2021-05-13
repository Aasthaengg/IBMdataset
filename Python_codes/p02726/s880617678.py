N, X, Y = map(int, input().split(' '))
dist = [[0 for _ in range(N + 10)] for _ in range(N + 10)]
dist[X][Y] = 1
res = [0 for i in range(N + 10)]
for i in range(1, N):
  for j in range(i + 1, N + 1):
    dist[i][j] = min(j - i, abs(j - X) + 1 + abs(i - Y), abs(j - Y) + 1 + abs(i - X))
    res[dist[i][j]] += 1
for i in range(1, N):
  print(res[i])