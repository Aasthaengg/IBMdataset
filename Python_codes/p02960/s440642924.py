import sys
input = sys.stdin.readline
S = list(input())[: -1]
mod = 10 ** 9 + 7
N = len(S)
dp = [[0] * 13 for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
  for j in range(13):
    if S[i] != "?":
      x = int(S[i])
      dp[i + 1][(j * 10 + x) % 13] += dp[i][j]
      dp[i + 1][(j * 10 + x) % 13] %= mod
    else:
      for x in range(10):
        dp[i + 1][(j * 10 + x) % 13] += dp[i][j]
        dp[i + 1][(j * 10 + x) % 13] %= mod
print(dp[-1][5])