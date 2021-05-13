n, k = map(int, input().split())
kkn = [list(map(int, input().split())) for _ in range(k)]
MOD = 998244353

dp = [0]*(n+1)
dp[1] = 1
dpac = [0]*(n+1)
dpac[1] = 1
for i in range(2, n+1):
    for kl, kr in kkn:
        l = i-kr
        r = i-kl
        if r < 0: continue
        l = max(l, 0)
        dp[i] += dpac[r] - dpac[l-1]
        dp[i] %= MOD
    dpac[i] = dpac[i-1] + dp[i]
    dpac[i] %= MOD
print(dp[n])