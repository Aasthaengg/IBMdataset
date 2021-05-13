n,k=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(k)]
mod=998244353


dp=[1]
imos=[0]*(2*n+10)
imos[0]=1
imos[1]=-1
for i in range(n):
    for l,r in lst:
        imos[i+l]+=dp[-1]
        imos[i+r+1]-=dp[-1]
    dp.append((dp[-1]+imos[i+1])%mod)


print(dp[n-1])