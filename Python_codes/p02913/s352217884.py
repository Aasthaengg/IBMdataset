import sys
readline = sys.stdin.readline

N = int(readline())
S = readline().rstrip()

# dp[i][j] = i文字目からとj文字目からとで最長の長さ
# S[i] != S[j] ならdp[i][j] = 0
# S[i] == S[j] ならdp[i][j] = dp[i + 1][j + 1] + 1

dp = [[0] * (N + 1) for i in range(N + 1)]

ans = 0
for i in range(N - 1, -1, -1):
  for j in range(N - 1, i, -1):
    if S[i] == S[j]:
      dp[i][j] = dp[i + 1][j + 1] + 1
      ans = max(ans, min(dp[i][j], j - i))
print(ans)