MOD = 998244353
n,k = map(int,input().split())
ns = [list(map(int,input().split())) for i in range(k)]
    
dp = [0 for j in range(n+1)]
cum = [0 for j in range(n+1)]
dp[1] = 1
cum[1] = 1
for i in range(2, n+1):
    for j in range(k):
        l, r = ns[j]
        if i - l >= 0:
            dp[i] += cum[i-l]
        if i - (r+1) >= 0:
            dp[i] -= cum[i-(r+1)]
    dp[i] = (dp[i] % MOD + MOD) % MOD
    cum[i] = (cum[i-1] + dp[i]) % MOD
print(dp[n])