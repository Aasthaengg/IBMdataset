def solve():
    L = input()
    N = len(L)
    mod = 10**9+7
    dp = [[0]*2 for _ in range(N+1)]
    dp[0][1] = 1
    for i in range(1,N+1):
        if L[i-1]=='1':
            dp[i][0] = dp[i-1][0]*3+dp[i-1][1]
            dp[i][1] = dp[i-1][1]*2
        else:
            dp[i][0] = dp[i-1][0]*3
            dp[i][1] = dp[i-1][1]
        dp[i][0]%=mod
        dp[i][1]%=mod
    ans = sum(dp[-1])%mod
    return ans
print(solve())