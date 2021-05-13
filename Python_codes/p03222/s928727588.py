def main():
    h,w,k=map(int,input().split())
    mod = 10**9+7
    b = [1,1,2,3,5,8,13,21,34]
    dp=[[0 for _ in range(w)]for j in range(h+1)]
    dp[0][0] = 1
    if w == 1:
        return 1

    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i+1][j]=(dp[i][j]*b[w-1]+dp[i][j+1]*b[w-2])%mod
            elif j == w-1:
                dp[i+1][j]=(dp[i][j]*b[w-1]+dp[i][j-1]*b[w-2])%mod
            else:
                dp[i+1][j]=(dp[i][j]*b[j]*b[w-1-j]+dp[i][j-1]*b[j-1]*b[w-1-j]+dp[i][j+1]*b[j]*b[w-2-j])%mod
    return dp[h][k-1]

print(main())