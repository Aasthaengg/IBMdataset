n,k=map(int,input().split())
lr=[tuple(map(int,input().split())) for i in range(k)]
mod=998244353
dp=[0]*n
dp[0]=1
s=0
for i in range(n):
  s+=dp[i]
  for l,r in lr:
    if i+l<n:
      dp[i+l]=(dp[i+l]+s)%mod
      if i+r+1<n:
        dp[i+r+1]=(dp[i+r+1]-s)%mod
print(dp[n-1])