K = int(input())
S = input()

MAX = 2020202
MOD = 10**9 + 7

fac = [0]*MAX
facinv = [0]*MAX
inv = [0]*MAX


def modinv(a, mod):
    b = mod
    x, u = 1, 0
    while b:
        q = a//b
        a, b = b, a-q*b
        x, u = u, x-q*u
    x %= mod
    return x


def mod_nCr_init(n, mod):
    fac[0] = fac[1] = 1
    facinv[0] = facinv[1] = 1
    inv[1] = 1
    for i in range(2, n):
        fac[i] = fac[i-1] * i % mod
        inv[i] = -inv[mod % i] * (mod // i) % mod
        facinv[i] = facinv[i-1] * inv[i] % mod


def mod_nCr(n, r, mod):
    if n < r or n < 0 or r < 0:
        return 0
    return fac[n] * (facinv[r] * facinv[n-r] % mod) % mod


mod_nCr_init(MAX, MOD)

ns = len(S)
ans = 0
for i in range(K+1):
    x = pow(26, i, MOD)
    x *= pow(25, K-i, MOD)
    x %= MOD
    x *= mod_nCr(ns+K-i-1, ns-1, MOD)
    ans += x
    ans %= MOD

print(ans)
