N, K = map(int, input().split(' '))
mod = 10 ** 9 + 7
fac = [0] * max(N + 1, 2 * K)
finv = [0] * max(N + 1, 2 * K)
inv = [0] * max(N + 1, 2 * K)
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2, max(N + 1, 2 * K)):
    fac[i] = fac[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    finv[i] = finv[i - 1] * inv[i] % mod


def comb(n, k):
    return (fac[n] * (finv[k] * finv[n - k]) % mod) % mod


for i in range(1, K+1):
    if i == 1:
        print(N - K + 1)
    elif i - 1 <= N - K:
        l = comb(K - 1, i - 1)
        r = comb(N - K + 1, i)
        print(l * r % mod)
    else:
        print(0)
