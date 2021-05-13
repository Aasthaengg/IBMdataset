N,M=list(map(int,input().split()))
inf=10**10
dp=[[inf]*(2**N) for _ in range(M+1)]
dp[0][0]=0

for i in range(M):
    a,b=list(map(int,input().split()))
    c=list(map(int,input().split()))

    s=0
    for cc in c:
        s+=2**(cc-1)
    
    for j in range(2**N):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
        dp[i+1][j|s]=min(dp[i+1][j|s],dp[i][j]+a)
    
print(dp[M][2**N-1] if dp[M][2**N-1]<inf else -1)
