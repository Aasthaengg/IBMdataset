
N, M, K = map(int, input().split())

MOD = 998244353
MAX = 5 * 10 ** 5 + 1

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


ans = 0
for k in range(K + 1):
    tmp = comb(N - 1, k) * M * pow(M - 1, N - k - 1, MOD) % MOD
    ans = (ans + tmp) % MOD
print(ans)
