def comb(n, k, MOD):
    if n < k:
        return 0
    if n - k < k:
        k = n - k
    comb = 1
    for x in range(n - k + 1, n + 1):
        comb = (comb * x) % MOD
    d = 1
    for x in range(1, k + 1):
        d = (d * x) % MOD
    comb *= pow(d, MOD - 2, MOD)
    return comb % MOD

n, k = map(int, input().split())
ans = 0
v = n
w = n - 1

ans = 1 + v * w
mod = 10 ** 9 + 7

for i in range(2, min(n,k) + 1):
    #print(f'v={v} n={n} i={i}')
    v = ((n - i + 1) * v)  * pow(i, mod - 2, mod)
    v %= mod
    w = ((n - i) * w) * pow(i, mod - 2, mod)
    w %= mod
    #print(v, w)
    ans += (v * w) % mod
    ans %= mod



print(ans)