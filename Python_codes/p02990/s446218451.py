def factorial_mod(n, mod):
    a = 1
    for i in range(1, n + 1):
        a *= i
        a %= mod
    return a


def cmb(n, k, mod):
    if k > n or k < 0:
        return 0
    fact_n = factorial_mod(n, mod)
    fact_k = factorial_mod(k, mod)
    fact_n_k = factorial_mod(n - k, mod)
    return (fact_n * pow(fact_k, mod - 2, mod) * pow(fact_n_k, mod - 2, mod)) % mod


n, k = map(int, input().split())
MOD = 10**9 + 7

for i in range(k):
    print(int(cmb(n - k + 1, i + 1, MOD) * cmb(k - 1, i, MOD) % MOD))