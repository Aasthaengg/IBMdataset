MOD = 10 ** 9 + 7
fac = [1] * (10 ** 5 + 10)
for i in range(len(fac) - 1):
    fac[i + 1] = fac[i] * (i + 1) % MOD


def comb(n, k):
    if n < 0:
        return 1
    if k < 0 or k > n:
        return 0
    return fac[n] * pow(fac[n - k], MOD - 2, MOD) * pow(fac[k], MOD - 2, MOD) % MOD


n, k = map(int, input().split())
for i in range(1, k + 1):
    ans = 0
    for j in range(i - 1, n - k + 1):
        ans += comb(j - 1, i - 2) * (n - k - j + 1)
    print(ans * comb(k - 1, i - 1) % MOD)
