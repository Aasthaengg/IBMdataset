def factorial(n, mod):
    fac = [0] * (n + 1)
    inv = [0] * (n + 1)
    fac[0], inv[0] = 1, 1
    for i in range(1, n + 1):
        fac[i] = fac[i-1] * i % mod
        inv[i] = inverse(fac[i], mod)
    return fac, inv

def inverse(a, mod):
    a %= mod # 除数が正なら正になる
    p = mod
    x, y = 0, 1
    while a > 0:
        n = p // a
        p, a = a, p % a, 
        x, y = y, x - n * y
    return x % mod # 除数が正なら正になる

mod = 10 ** 9 + 7
x, y = map(int, input().split())
if (x + y) % 3 != 0:
    print(0)
    quit()
n = (x + y) // 3
if x < n or y < n:
    print(0)
    quit()

m = min(x, y) - n
fac, inv = factorial(n, mod)
print(fac[n] * inv[n-m] * inv[m] % mod) # nCm
