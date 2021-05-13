n,s=map(int,input().split())
A=list(map(int,input().split()))
mod=998244353
a=499122177
b=pow(2,n-1,mod)
dp=[[0]*(s+1) for i in range(n+1)]
for i in range(n+1):
  dp[0][0]=pow(2,n,mod)
for i in range(1,n+1):
  dp[i]=dp[i-1][0:s+1]
  for j in range(s+1):
    if j+A[i-1]>s:
      break
    dp[i][j+A[i-1]]=(dp[i-1][j+A[i-1]]+dp[i-1][j]*a)%mod
print(dp[-1][-1])