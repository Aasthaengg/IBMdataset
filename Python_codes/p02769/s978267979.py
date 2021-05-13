
N, K = map(int, input().split())

MAX = 6 * 10 ** 5 + 1
MOD = 10 ** 9 + 7

# Factorial
fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1

# Inverse
inv = [0] * (MAX + 1)
inv[1] = 1

# Inverse factorial
finv = [0] * (MAX + 1)
finv[0] = 1
finv[1] = 1

for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, k):
    if n < k or k < 0:
        return 0
    return (fac[n] * finv[k] * finv[n - k]) % MOD


def comb_rep(n, k):
    return comb(n + k - 1, n - 1)


if K >= N - 1:
    print(comb_rep(N + 1, N - 1))
else:
    ans = 0
    for i in range(K + 1):
        ans += comb(N, i) * comb_rep(N - i, i) % MOD
        ans %= MOD
    print(ans)
