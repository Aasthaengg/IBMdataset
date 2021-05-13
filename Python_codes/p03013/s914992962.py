N,M=map(int,input().split())
mod=1000000007
a=[0]*(10**5+1)
dp=[0]*(10**5+1)
for i in range(M):
    b=int(input())
    a[b]=1
dp[0]=1
for i in range(1,N+1):
    if a[i]==1:
        continue
    dp[i]+=dp[i-1]
    if i>1:
        dp[i]+=dp[i-2]
    dp[i]=dp[i]%mod
print(dp[N]%mod)
