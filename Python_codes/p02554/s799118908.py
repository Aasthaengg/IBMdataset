def modpow(a, n, mod):
    res = 1
    while n:
        if n % 2:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


MOD = 1000000007

n = int(input())
ans = (modpow(10, n, MOD) - 2 * modpow(9, n, MOD) + modpow(8, n, MOD)) % MOD
print(ans)
