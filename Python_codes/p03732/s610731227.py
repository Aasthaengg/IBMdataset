N, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(N)]

DP = [[0] * (3 * N + 1) for _ in range(N + 1)]

for i in range(N):
  for j in range(i, -1, -1):
    for k in range(3 * i, -1, -1):
      kk = k + wv[i][0] - wv[0][0]
      DP[j + 1][kk] = max(DP[j + 1][kk], DP[j][k] + wv[i][1])

ans = 0
for i in range(N + 1):
  if i * wv[0][0] > W:
    break
  for j in range(3 * N + 1):
    if i * wv[0][0] + j > W:
      break
    ans = max(ans, DP[i][j])

print(ans)