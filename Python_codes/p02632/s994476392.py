mod = 10 ** 9 + 7

SIZE = 2 * 10 ** 6 + 5
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


k = int(input())
S = input()
s_length = len(S)
full_length = len(S) + k
ans = 0
for i in range(k+1):
    add = pow(26, i, mod) * pow(25, k-i, mod) * nCr(full_length-i-1, s_length-1) % mod
    ans = (ans + add) % mod

print(ans)

