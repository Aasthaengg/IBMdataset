def main():
    n,ma,mb = map(int,input().split())
    dp = [[[float("inf") for _ in range(401)] for _ in range(401)] for _ in range(n+1)]
    dp[0][0][0]=0

    for i in range(1,n+1):
        a,b,c = map(int,input().split())
        for j in range(401):
            for k in range(401):
                if a<=j and b<=k:
                    dp[i][j][k] = min(dp[i-1][j][k],dp[i-1][j-a][k-b]+c)
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    ans = float("inf")
    for i in range(1,401):
        for j in range(1,401):
            if i*mb == j*ma:
                ans = min(ans,dp[n][i][j])
    if ans==float("inf"):
        print(-1)
    else:
        print(ans)
if __name__ == "__main__":
    main()
