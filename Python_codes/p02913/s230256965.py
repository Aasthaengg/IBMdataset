N = int(input())
S = list(input())
dp = [[0]*N for _ in range(N)]
dp[N-1][N-1] = 1
for i in range(N-1, -1, -1):
  if S[i] == S[-1]:
    dp[N-1][i] = 1

for i in range(N-1, -1, -1):
  if S[i] == S[-1]:
    dp[i][N-1] = 1

for i in range(N-1, 0, -1):
  for j in range(N-1, 0, -1):
    if S[i-1] == S[j-1]:
      dp[i-1][j-1] = dp[i][j] + 1

ans = 0
for i in range(N):
  for j in range(i+1, N):
    ans = max(ans, min(dp[i][j], j-i))
print(ans)