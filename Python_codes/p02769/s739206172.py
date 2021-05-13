N, K = map(int, input().split())

MOD = 10 ** 9 + 7
MAX = 4 * 10 ** 5 + 10
modinv = lambda a, mod=MOD: pow(a, mod - 2, mod)
fac, inv = [1] * MAX, [1] * MAX
for i in range(1, MAX):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = modinv(fac[i])
comb = lambda n, k: fac[n] * inv[k] * inv[n - k] % MOD

if K >= N - 1:
    print(comb(2 * N - 1, N - 1))
else:
    ans = 0
    for i in range(K + 1):
        ans = (ans + comb(N - 1, N - 1 - i) * comb(N, i)) % MOD
    print(ans)
