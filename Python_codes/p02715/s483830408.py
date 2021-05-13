n, k = map(int, input().split())

mod = 10 ** 9 + 7

def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x % mod
        x = x * x % mod
        n //= 2

    return K * x % mod


memo = {}
ans = 0

for x in reversed(range(1, k + 1)):
    memox = pow_k((k // x), n)
    for i in range(2, k // x + 1):
        memox -= memo[i * x]
        memox %= mod
    memo[x] = memox
    ans += x * memox % mod
    ans %= mod

print(ans)
