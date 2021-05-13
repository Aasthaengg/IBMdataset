def comb(n, r, p):
    x, y = 1, 1
    for i in range(n, n - r, -1):
        x *= i
        y *= i + r - n
        x %= p
        y %= p
    return pow(y, p - 2, p) * x % p

n, m, k = map(int, input().split())
mod = 998244353
all = pow(n, m, mod)
x, y = [0] * (k + 1), [0] * (k + 1)
x[0] = (m * pow(m - 1, n - k - 1, mod)) % mod
y[0] = 1
for i in range(1, k + 1):
    x[i] = (x[i - 1] * (m - 1)) % mod
    y[i] = (pow(i, mod - 2, mod) * y[i - 1] * (n - i)) % mod
y.reverse()
ans = 0
for i in range(k + 1):
    ans += x[i] * y[i]
    ans %= mod
print(ans)