import sys
readline = sys.stdin.readline

N = int(readline())
S = readline().rstrip()

dp = [[0] * (N + 1) for i in range(N + 1)]

ans = 0
for i in range(N - 1, -1, -1):
  for j in range(N - 1, i, -1):
    if S[i] == S[j]:
      dp[i][j] = dp[i + 1][j + 1] + 1
      if dp[i][j] > j - i:
        dp[i][j] = j - i
      if ans < dp[i][j]:
        ans = dp[i][j]
print(ans)