n = int(input())
c = [int(input()) for _ in range(n)]

mod = 10**9 + 7

if n <= 2:
    print(1)
    exit()

# 圧縮
a = [c[0]]
m = 1
for c1, c2 in zip(c, c[1:]):
    if c2 != c1:
        a.append(c2)
        m += 1

memo = [-1] * (2 * 10**5 + 1)
ans = 1
dp = [0] * (m+1)
dp[0] = 1

for i in range(m):
    if memo[a[i]] == -1:
        memo[a[i]] = i
        dp[i+1] = dp[i]
    else:
        idx = memo[a[i]] + 1
        dp[i+1] += dp[i] + dp[idx]
        dp[i+1] %= mod
        memo[a[i]] = i

print(dp[m] % mod)