n, m, k = map(int, input().split())

MOD = 998244353


def prepare(n, MOD):
    fac = [None] * (n + 2)
    finv = [None] * (n + 2)
    inv = [None] * (n + 2)
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, n + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
    return fac, finv


def combination(n, k, fac, finv, MOD):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    else:
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


fac, finv = prepare(n, MOD)

ans = 0
for i in range(k + 1):
    ans += combination(n - 1, i, fac, finv, MOD) * m * pow(m - 1, n - i - 1, MOD)
    ans %= MOD

print(ans)
