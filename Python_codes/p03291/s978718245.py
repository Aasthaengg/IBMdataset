s = input()
n = len(s)
mod = 10**9+7
cnt = 0
dp = [[0 for i in range(4)] for j in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
  if s[i-1] in "A?":
    dp[i][1] += dp[i-1][0]
  if s[i-1] in "B?":
    dp[i][2] += dp[i-1][1]
  if s[i-1] in "C?":
    dp[i][3] += dp[i-1][2]
  for j in range(4):
    if s[i-1] == "?":
      dp[i][j] += dp[i-1][j]*3
    else:
      dp[i][j] += dp[i-1][j]
    dp[i][j] %= mod
print(dp[-1][-1])