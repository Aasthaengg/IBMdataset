MOD = 10**9+7
def solve(n):
    """
    0: {}
    1: {0}
    2: {9}
    3: {0,9}
    """
    dp = [[0]*4 for i in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        dp[i+1][3] = (10*dp[i][3] + dp[i][2] + dp[i][1]) % MOD
        dp[i+1][2] = (9*dp[i][2] + dp[i][0]) % MOD
        dp[i+1][1] = (9*dp[i][1] + dp[i][0]) % MOD
        dp[i+1][0] = (8*dp[i][0]) % MOD
    return dp[n][3]

n = int(input())
print(solve(n))