H,W,K=map(int,input().split())

fibonacchi=[1 for i in range(0,W+1)]
for i in range(0,W+1):
    if i>=2:
        fibonacchi[i]=fibonacchi[i-1]+fibonacchi[i-2]

dp=[[[0 for i in range(0,W+1)] for j in range(0,W+1)] for k in range(0,H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        for k in range(1,W+1):
            if i==1:
                if j==k:
                    dp[i][j][k]=fibonacchi[j-1]*fibonacchi[W-k]
                elif j==k-1:
                    dp[i][j][k]=fibonacchi[j-1]*fibonacchi[W-k]
                elif j==k+1:
                    dp[i][j][k]=fibonacchi[k-1]*fibonacchi[W-j]
            else:
                ans=0
                if k>=2:
                    ans+=dp[i-1][j][k-1]*dp[1][k-1][k]
                if W-1>=k:
                    ans+=dp[i-1][j][k+1]*dp[1][k+1][k]
                ans+=dp[i-1][j][k]*dp[1][k][k]
                dp[i][j][k]=ans

print(dp[H][1][K]%(10**9+7))
