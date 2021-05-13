S = int(input())

cnt = 1
res = 0
mod = 10 ** 9 + 7

MAX = 3000
MOD = 1000000007

fac = [None] * MAX
finv = [None] * MAX
inv = [None] * MAX

def comb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

def comb(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

comb_init()

while S >= cnt * 3:
    tmp = S - (cnt * 3)
    res += comb(tmp + cnt - 1, cnt - 1)
    res %= MOD
    cnt += 1

print(res)

