N = int(input())
S = list(input())
dp = [[0]*(N) for _ in range(N)]
for i in range(N):
  if S[-1] == S[i]:
    dp[-1][i] = 1
    dp[i][-1] = 1
  

for i in range(N-2, -1, -1):
  for j in range(N-2, -1, -1):
    if S[i] == S[j]:
      dp[i][j] = dp[i+1][j+1] + 1
ans = 0
for i in range(N):
  for j in range(N):
    if i + dp[i][j] <= j:
      ans = max(ans, dp[i][j])
print(ans)