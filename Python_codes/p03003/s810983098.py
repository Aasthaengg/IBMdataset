n,m=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
dp=[[0]*m for _ in range(n)]
sum=[[0]*m for _ in range(n)]
mod=10**9+7
for i in range(n):
  if s[i]==t[0]:
    dp[i][0]=1
  else:
    dp[i][0]=0
for i in range(m):
  if t[i]==s[0]:
    dp[0][i]=1
  else:
    dp[0][i]=0
sum[0][0]=dp[0][0]
for i in range(1,n):
  sum[i][0]=sum[i-1][0]+dp[i][0]
for i in range(1,m):
  sum[0][i]=sum[0][i-1]+dp[0][i]
for i in range(1,n):
  for j in range(1,m):
    if s[i]==t[j]:
      dp[i][j]=(sum[i-1][j-1]+1)%mod
    else:
      dp[i][j]=0
    sum[i][j]=(sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+dp[i][j])%mod
ans=0
for i in range(n):
  for j in range(m):
    ans+=dp[i][j]
    ans=ans%mod
print((ans+1)%mod)