MOD = 10 ** 9 + 7
s = input()
n = len(s)
dp = [[0] * 4 for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
  if s[i] == '?':
    dp[i + 1][0] += dp[i][0] * 3
    dp[i + 1][0] %= MOD
  else:
    dp[i + 1][0] += dp[i][0]
  for j in range(3):
    if s[i] == 'ABC'[j] or s[i] == '?':
      dp[i + 1][j + 1] += dp[i][j]
    dp[i + 1][j + 1] += dp[i][j + 1] * (3 if s[i] == '?' else 1)
    dp[i + 1][j + 1] %= MOD
print(dp[n][3] % MOD)