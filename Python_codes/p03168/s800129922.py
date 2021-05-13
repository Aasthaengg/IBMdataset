n = int(input())
p = list(map(float, input().split()))
dp = [[0] * (2*n + 2) for i in range(n//2+1)]
dp[0][n+1] = p[0]
dp[0][n] = 1-p[0]
for i in range(n//2):
  p1, p2 = p[2*i+1], p[2*i+2]
  h,t = p1*p2,(1-p1) * (1-p2)
  m = 1 - h - t
  for j in range(n-i,n+i+2):
    plus = dp[i][j]
    dp[i+1][j+1] += plus * h
    dp[i+1][j] += plus * m
    dp[i+1][j-1] += plus * t
print(sum(dp[n//2][n+1:]))