n, t = map(int, input().split())
a, b = [0] * n, [0] * n
for i in range(n):
  a[i], b[i] = map(int, input().split())

dp = [[[0] * (t+1) for i in range(n+1)] for j in range(2)]
for i in range(n):
  for d in range(2):
    for l in range(1,t+1):
      if(l < a[i]):
        dp[d][i+1][l] = max(dp[d][i][l], d*(b[i]+dp[0][i][l-1]))
      else:
        dp[d][i+1][l] = max(dp[d][i][l], b[i]+dp[d][i][l-a[i]], d*(b[i]+dp[0][i][l-1]))

print(dp[1][n][t])