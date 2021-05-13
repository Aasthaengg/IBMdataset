MOD = 10**9 + 7
l = input()
dp = [1, 0] # bounded, unbounded
ndp = [0, 0]

for c in l:
    ndp1 = dp[1] * 3
    if c == '1':
        ndp0 = dp[0] * 2
        ndp1 += dp[0]
    else:
        ndp0 = dp[0]
    dp = ndp0 % MOD, ndp1 % MOD
print(sum(dp) % MOD)
