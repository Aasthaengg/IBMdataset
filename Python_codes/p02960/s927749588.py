s=list(input())
n=len(s)
s.reverse()
mod=10**9+7
dp=[[0]*13 for i in range(n+1)]
dp[0][0]=1
x=1
for i in range(n):
  for j in range(13):
    if s[i]=='?':
      for k in range(10):
        dp[i+1][j]+=dp[i][(j-(k*x)%13+13)%13]
    else:
      dp[i+1][j]+=dp[i][(j-(int(s[i])*x)%13+13)%13]
    dp[i+1][j]%=mod
  x*=10
  x%=13
print(dp[n][5])