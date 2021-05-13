n, k = map(int, input().split())
s = []
for i in range(k):
    l, r = map(int, input().split())
    s.append([l, r])

mod = 998244353
dp = [0] * (n+1)
cumsum = [0] * (n+1)

dp[1] = 1
s = sorted(s)
counter = 0
for i in range(1, n+1):
    counter += cumsum[i]
    dp[i] += counter
    dp[i] %= mod
    for l, r in s:
        if i+l <= n:
            cumsum[i+l] += dp[i]
        if i+r+1 <= n:
            cumsum[i+r+1] -= dp[i]
print(dp[n] % mod)