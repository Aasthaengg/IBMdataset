N = int(input())
S = input()

dp = [[0]*N for _ in range(N)]
for i in range(1, N):
  if S[i] == S[0]:
    dp[0][i] = 1

for i in range(1, N-1):
  for j in range(i+1, N):
    if S[i] == S[j]:
      if dp[i-1][j-1] == j - i:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = dp[i-1][j-1] + 1

ans = 0
for i in range(N):
  ans = max(ans, max(dp[i]))

print(ans)