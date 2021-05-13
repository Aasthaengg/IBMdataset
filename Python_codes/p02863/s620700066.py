n, t = map(int, input().split())
ab = sorted([ list(map(int, input().split())) for _ in range(n)])
A, B = zip(*ab)
dp = [[0]*(t+1) for _ in range(n+1)]
for i in range(n):
  for j in range(t+1):
    if A[i] >= j:
      dp[i+1][j] = dp[i][j]
    else:
      dp[i+1][j] = max(dp[i][j-A[i]] + B[i], dp[i][j])
maxB = [B[-1]]*n
for i in range(n-2, 0, -1):
  maxB[i] = max(B[i], maxB[i+1])
ans = 0
for i in range(n-1):
  ans = max(ans, dp[i+1][t] + maxB[i+1])
print(ans)