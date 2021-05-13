n, k = map(int, input().split())
a = list(map(int, input().split()))
b = a + a
c = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            c += 1
d = 0
for i in range(len(b)):
    for j in range(i + 1, len(b)):
        if b[i] > b[j]:
            d += 1
d -= c * 2
def modpow(n, p, mod):
    r = 1
    while p > 0:
        if p & 1 == 1:
            r = r * n % mod
        n = n * n % mod
        p >>= 1
    return r
def modinv(n, mod):
    return modpow(n, mod - 2, mod)
MOD = 10 ** 9 + 7
ans = (k - 1) * d % MOD
ans += 2 * c
ans %= MOD
ans *= k
ans %= MOD
ans *= modinv(2, MOD)
ans %= MOD
print(ans)