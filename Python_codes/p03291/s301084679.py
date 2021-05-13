MOD = 10 ** 9 + 7
dp = [0, 0]
ans = 0
t = 1
for c in input():
    ndp = dp.copy()
    if c in 'A':
        ndp[0] = (dp[0] + t) % MOD
    elif c in 'B':
        ndp[1] = (ndp[1] + dp[0]) % MOD
    elif c in 'C':
        ans = (ans + dp[1]) % MOD
    else:
        ndp[0] = (3 * dp[0] + t) % MOD
        ndp[1] = (3 * dp[1] + dp[0]) % MOD
        ans = (3 * ans + dp[1]) % MOD
        t = (t * 3) % MOD
    #print(*ndp, ans)
    dp = ndp
print(ans)