n,k=map(int,input().split())
mod=998244353
R=[]
for _ in range(k):
  l,r=map(int,input().split())
  R.append([l,r])

dp=[0 for _ in range(n+1)]
dp[1]=1
dpsum=[0 for _ in range(n+1)]
dpsum[1]=1
for i in range(2,n+1):
  for j in range(k):
    li=i-R[j][1]
    ri=i-R[j][0]
    if ri<0:
      continue
    li=max(li,1)
    dp[i]+=(dpsum[ri]-dpsum[li-1])%mod
  dpsum[i]=dpsum[i-1]+dp[i]
  dpsum[i]%=mod
print(dp[n]%mod)