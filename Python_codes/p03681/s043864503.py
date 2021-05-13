n,m=map(int,input().split())
dp=[1]
for i in range(1,10**5+1):
  dp.append(dp[-1]*i%(10**9+7))
if n==m:
  print((2*(dp[n]**2))%(10**9+7))
elif n+1==m:
  print(dp[n]*dp[m]%(10**9+7))
elif m+1==n:
  print(dp[m]*dp[n]%(10**9+7))
else:
  print(0)