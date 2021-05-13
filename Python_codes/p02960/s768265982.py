# D - Digits Parade
# https://atcoder.jp/contests/abc135/tasks/abc135_d

S = input()
n = len(S)

MOD = 10 ** 9 + 7

# dp[i][j] i桁目まででj余る数
dp = [[0] * 13 for _ in range(n + 1)]
dp[0][0] = 1

for i, s in enumerate(S):
  for j in range(10):
    if s == "?" or int(s) == j:
      for k in range(13):
        dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
  for k in range(13):
    dp[i + 1][k] %= MOD

print(dp[n][5])
