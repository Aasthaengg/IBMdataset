n,m=map(int,input().split())

a=[int(input()) for _ in range(m)]

dp=[0]*(n+1)

broken=[0]*(n+1)

for aa in a:
    broken[aa]=1

dp[0]=1
if broken[1]==0:
    dp[1]=1

mod=10**9+7

for i in range(2,n+1):
    if broken[i]==0:
        dp[i]=(dp[i-1]+dp[i-2])%mod

print(dp[-1])

