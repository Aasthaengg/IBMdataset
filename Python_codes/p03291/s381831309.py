s = input().strip()
MOD = pow(10, 9) + 7
# dp: dp[0][...] = ABCカウントを更新しない時の数
# dp: dp[1][...] = Aまで合わせた時の数
# dp: dp[2][...] = Bまで合わせた時の数
# dp: dp[3][...] = Cまで合わせた時の数
dp = [[0 for _ in range(len(s) + 1)] for _ in range(4)]
dp[0][0] = 1

for i, _s in enumerate(s):
  if _s == '?':
    dp[0][i+1] += dp[0][i] * 3 % MOD
    dp[1][i+1] += dp[1][i] * 3 % MOD
    dp[2][i+1] += dp[2][i] * 3 % MOD
    dp[3][i+1] += dp[3][i] * 3 % MOD
    dp[0][i+1] %= MOD
    dp[1][i+1] %= MOD
    dp[2][i+1] %= MOD
    dp[3][i+1] %= MOD
  else:
    dp[0][i+1] += dp[0][i]
    dp[1][i+1] += dp[1][i]
    dp[2][i+1] += dp[2][i]
    dp[3][i+1] += dp[3][i]
    dp[0][i+1] %= MOD
    dp[1][i+1] %= MOD
    dp[2][i+1] %= MOD
    dp[3][i+1] %= MOD
  if _s == 'A' or _s == '?':
    dp[1][i+1] += dp[0][i]
    dp[1][i+1] %= MOD
  if _s == 'B' or _s == '?':
    dp[2][i+1] += dp[1][i]
    dp[2][i+1] %= MOD
  if _s == 'C' or _s == '?':
    dp[3][i+1] += dp[2][i]
    dp[3][i+1] %= MOD

print(dp[3][-1])
