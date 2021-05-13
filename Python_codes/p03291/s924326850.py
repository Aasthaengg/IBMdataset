import numpy as np
MOD = 10**9 + 7
def solve(s):
    n = len(s)
    dp = np.zeros((n+1, 4), dtype=int)
    dp[0,0] = 1
    for i in range(n):
        t = 2 * int(s[i] == "?") + 1
        dp[i+1] = t * dp[i] % MOD
        if s[i] == "A":
            dp[i+1,1] += dp[i,0]
        elif s[i] == "B":
            dp[i+1,2] += dp[i,1]
        elif s[i] == "C":
            dp[i+1,3] += dp[i,2]
        else:
            dp[i+1,1:] += dp[i,:-1]
    return dp[n][3] % MOD

s = input()
print(solve(s))