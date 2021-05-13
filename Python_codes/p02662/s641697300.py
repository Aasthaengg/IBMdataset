n, s = map(int, input().split())
a = list(map(int, input().split()))

mod = 998244353

dp = [[0] * 4000 for _ in range(4000)]

def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x % mod
        x *= x % mod
        n //= 2

    return K * x % mod

inv2 = pow_k(2, mod - 2)
pow2n = pow_k(2, n)

dp[0][0] = pow2n
for i in range(1, n + 1):
    for j in range(s + 1):
        if j >= a[i - 1]:
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - a[i - 1]] * inv2 % mod) % mod
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][s])
