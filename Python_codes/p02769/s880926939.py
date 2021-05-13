n, k = map(int, input().split())
mod = 10**9 + 7

SIZE = 2 * 10 ** 5 + 1
fact = [0] * SIZE
inv = [0] * SIZE
finv = [0] * SIZE
fact[0], fact[1] = 1, 1
inv[1] = 1
finv[0], finv[1] = 1, 1
for i in range(2, SIZE):
    fact[i] = fact[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    finv[i] = finv[i - 1] * inv[i] % mod


def nCr(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    return fact[n] * (finv[r] * finv[n - r] % mod) % mod


ans = 1
limit = min(k+1, n)
for i in range(1, limit):
    vacant = i
    fill = n-i
    add = i
    pattern = nCr(n, vacant) * nCr(add+fill-1, add)
    ans = (ans + pattern) % mod

print(ans)