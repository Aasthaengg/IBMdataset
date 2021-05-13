n = int(input())
S = input()
dp = [[0]*n for _ in range(n)]
for i in range(n-1, -1, -1):
  for j in range(n-1, -1, -1):
    if i == n-1:
      dp[i][j] = int(S[i] == S[j])
    elif j == n-1:
      dp[i][j] = dp[j][i]
    else:
      if S[i] == S[j]:
        dp[i][j] = dp[i+1][j+1] + 1
ans = 0
for i in range(n):
  for j in range(n):
    ans = max(ans, min(dp[i][j], j-i))
print(ans)