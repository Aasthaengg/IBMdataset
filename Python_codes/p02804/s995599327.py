n, k = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort()
mod = 10 ** 9 + 7
ans = 0

f = [1] * (n + 1)
inv = [1] * (n + 1)
for i in range(1, n + 1):
    f[i] = (f[i - 1] * i) % (mod)
inv[n] = pow(f[n], mod - 2, mod)
for i in range(n - 1, 0, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod

def combination(n, r):
    if (n != 0) & (n >= r):
        return f[n] * inv[r] * inv[n - r] % mod
    return 0    
    
ans = 0
for index, value in enumerate(a):
    ans += (combination(index, k - 1) - combination(n - index - 1, k - 1)) * value
print(ans % mod)