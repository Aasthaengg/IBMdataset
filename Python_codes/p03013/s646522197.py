N, M = map(int,input().split())
oks = [True]*(N+1)
mod = 1e9+7
for i in range(M):
    a = int(input())
    oks[a]=False
dp = [0]*(N+1)
dp[0]=1
if oks[1]:
    dp[1]=1
else:
    dp[1]=0
for i in range(2,N+1):
    if oks[i]:
        dp[i]=dp[i-1]+dp[i-2]
        dp[i]%=mod
print(int(dp[N]))