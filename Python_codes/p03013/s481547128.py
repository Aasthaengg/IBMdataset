N,M=map(int,input().strip().split())
a=[int(input()) for _ in range(M)]

danger=[0 for n in range(N+1)]
for m in range(M):
    danger[a[m]]=1

dp=[0 for n in range(N+1)]
dp[0]=1
if danger[1]!=1:
    dp[1]=1
for n in range(2,N+1):
    if danger[n]==1:
        dp[n]=0
    else:
        dp[n]=dp[n-1]+dp[n-2]

print(dp[N]%1000000007)