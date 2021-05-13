N = int(input())
p = [0]
p += list(map(float, input().split(' ')))
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
dp[1][0], dp[1][1] = 1- p[1], p[1]
for i in range(2, N + 1):
  for j in range(i + 1):
      dp[i][j] = dp[i-1][j-1]  * p[i]
      dp[i][j] += dp[i-1][j] * (1 - p[i])
res = 0
for i in range(N // 2 + 1, N + 1):
  res += dp[N][i]
print(res)