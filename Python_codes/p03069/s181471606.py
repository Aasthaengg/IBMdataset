n = int(input())
s = list(input())
dp = [ [0]*n for _ in range(2) ]
if s[0] == ".":
  dp[1][0] = 1
else:
  dp[0][0] = 1
for i in range(n-1):
  if s[i+1] == ".":
    dp[0][i+1] = dp[0][i]
    dp[1][i+1] = min(dp[0][i], dp[1][i]) + 1
  else:
    dp[0][i+1] = dp[0][i] + 1
    dp[1][i+1] = min(dp[0][i], dp[1][i])
print(min(dp[0][n-1], dp[1][n-1]))