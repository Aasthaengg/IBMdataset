N, K = map(int, open(0).read().split())

MAX = 5 * 10 ** 5
MOD = 10 ** 9 + 7

# Factorial
fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1
for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD
    
# Inverse factorial
finv = [0] * (MAX + 1)
finv[MAX] = pow(fac[MAX], MOD - 2, MOD)
for i in reversed(range(1, MAX + 1)):
    finv[i - 1] = finv[i] * i % MOD

def comb(n, k):
    return fac[n] * finv[n - k] * finv[k]

def rep_perm(n, k):
    return comb(n + k - 1, k)

ans = 0
for k in range(0, min(N, K + 1)):
    ans += comb(N, k) * rep_perm(N - k, k)
    ans %= MOD
print(ans)
