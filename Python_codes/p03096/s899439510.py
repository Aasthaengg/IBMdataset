N=int(input())
dp=[1 for i in range(0,N)]
data={i:-1 for i in range(1,2*10**5+1)}
mod=10**9+7

c=int(input())
data[c]=0

for i in range(1,N):
    c=int(input())
    if data[c]==i-1:
        dp[i]=dp[i-1]
    elif data[c]==-1:
        dp[i]=dp[i-1]
    else:
        dp[i]=(dp[i-1]+dp[data[c]])%mod
    data[c]=i

print(dp[N-1])
