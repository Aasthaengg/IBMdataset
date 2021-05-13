n, t = map(int, input().split())
l = []
 
for i in range(n):
  a, b = map(int, input().split())
  l.append((a, b))
 
l.sort()
 
ans = 0
dp = [[0]*t for _ in range(n+1)]
for i in range(n):
  cur = dp[i][t-1] + l[i][1]
  ans = max(ans, cur)
  for j in range(t):
    dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    nj = j+l[i][0]
    if nj < t:
      dp[i+1][nj] = max(dp[i+1][nj], dp[i][j]+l[i][1])
print(ans)