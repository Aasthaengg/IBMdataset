mod = 998244353
n, m, k = map(int, input().split())


def modpow(a, n, mod):
    y = 1
    while n:
        if n & 1:
            y = y * a % mod
        a = a * a % mod
        n >>= 1
    return y

MAX = 500000
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


mod_nCr_init(MAX, mod)


ans = 0
for i in range(0, k+1):
    ans += m * modpow(m-1, n-1-i, mod) * mod_nCr(n-1, i, mod)
    ans %= mod

print(ans)
