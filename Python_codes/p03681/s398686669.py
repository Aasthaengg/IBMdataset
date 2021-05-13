def factorial(x, mod):
    ret = 1
    while x > 0:
        ret = (ret * x) % mod
        x -= 1
    return ret


MOD = 10**9 + 7
N, M = map(int, input().split())

if N == M:
    print((2 * factorial(N, MOD) * factorial(M, MOD)) % MOD)
elif abs(N - M) == 1:
    print((factorial(N, MOD) * factorial(M, MOD)) % MOD)
else:
    print(0)
