MOD = 10**9 + 7
n, m = [int(item) for item in input().split()]
s = [int(item) for item in input().split()]
t = [int(item) for item in input().split()]

dp = [[0] * (n+1) for _ in range(m+1)]
for i, tt in enumerate(t):
    val = 0 
    for j, ss in enumerate(s):
        # Update Partial
        if ss == tt:
            val += dp[i][j] + 1
            val %= MOD
        # Keep prev
        dp[i+1][j+1] += dp[i][j+1] + val
        dp[i+1][j+1] %= MOD 
print((dp[m][n]+1) % MOD)
