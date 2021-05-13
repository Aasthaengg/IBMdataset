MOD = 10**9 + 7
dp = [-1] * 2001
dp[0] = 1
dp[1] = 0
dp[2] = 0

def f(n):
    for i in range(3, n+1):
        dp[i] = sum(dp[i-j] for j in range(3, i+1)) % MOD
    return dp[n]

assert f(7) == 3
assert f(2) == 0
assert f(1729) == 294867501

s = int(input())
print(f(s))