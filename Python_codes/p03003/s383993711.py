N,M=map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
dp=[[0]*(M+1) for i in range(N+1)]
mod=10**9+7
for n in range(1,N+1):
    for m in range(1,M+1):
        x=1 if S[n-1]==T[m-1] else -dp[n-1][m-1]
        y=dp[n-1][m]+dp[n][m-1]+x
        dp[n][m]=y if y<mod else y-mod
print((dp[-1][-1]+1)%mod)