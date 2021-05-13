def factorial(n, mod):
    fac = [0] * (n + 1)
    inv = [0] * (n + 1)
    fac[0], inv[0] = 1, 1
    for i in range(1, n + 1):
        fac[i] = fac[i-1] * i % mod
        inv[i] = inverse(fac[i], mod)
    return fac, inv

def inverse(a, mod):
    a %= mod
    p = mod
    x, y = 0, 1
    while a > 0:
        n = p // a
        p, a = a, p % a, 
        x, y = y, x - n * y
    return x % mod

n, k = map(int, input().split())
mod = 10 ** 9 + 7
fac, inv = factorial(n, mod)

if k == 1:
    print(n * (n - 1) // 2 % mod)
    quit()

if k >= n:
    k = n - 1
ans = 0
for i in range(0, k + 1):
    nci = fac[n] * inv[n-i] % mod * inv[i] % mod
    mci = fac[n-1] * inv[n-1-i] % mod * inv[i] % mod
    ans = (ans + nci * mci % mod) % mod
print(ans)
