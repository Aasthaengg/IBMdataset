MAX = 2000
MOD = 10**9+7

fac = [0] * (MAX+1)
finv = [0] * (MAX+1)
inv = [0] * (MAX+1)

def comb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX+1):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD

def comb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD


if __name__ == '__main__':
    n, k = map(int, input().split())
    comb_init()
    for i in range(1, k+1):
        print(comb(n-k+1, i) * comb(k-1, i-1) % MOD)
