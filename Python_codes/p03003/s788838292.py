n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
dp = [0 for i in range(m)]
mod = 10 ** 9 + 7
for si in s:
    memo = [0]
    for i, ti in enumerate(t):
        memo.append((memo[-1] + dp[i]) % mod)
    for i, ti in enumerate(t):
        if si == ti:
            dp[i] += memo[i] + 1
            dp[i] %= mod

ans = 1
for dpi in dp:
    ans += dpi
    ans %= mod
print(ans)
