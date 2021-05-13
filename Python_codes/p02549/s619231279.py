n,k=map(int,input().split())
mod=998244353
l=[0]*n
r=[0]*n
for i in range(k):
  l[i],r[i]=map(int,input().split())
dp=[0]*(n+10)
dp[0]=1
sumdp=[0]*(n+10)
sumdp[1]=1
for i in range(1,n):
  for j in range(k):
    li=max(0,i-r[j])
    ri=max(0,i-l[j]+1)
    dp[i]+=sumdp[ri]-sumdp[li]
  sumdp[i+1]=(sumdp[i]+dp[i])%mod
print(dp[n-1]%mod)