mod=998244353
n,k=map(int,input().split())
l,r=[0]*k,[0]*k
for i in range(k):
  l[i],r[i]=map(int,input().split())
dp=[0]*(n+1)
sumdp=[0]*(n+1)
dp[1]=1
sumdp[1]=1
for i in range(2,n+1):
  for j in range(k):
    lj=max(i-r[j],0)
    rj=max(i-l[j],0)
    dp[i]+=sumdp[rj]-sumdp[lj-1]
    dp[i]%=mod
  sumdp[i]=sumdp[i-1]+dp[i]
  sumdp[i]%=mod
print(dp[n])