MOD = 10**9 + 7


def fact(n, MOD):
    res = 1
    for i in range(1, n + 1):
        res *= i
        res %= MOD
    return res


N, M = map(int, input().split())
ans = 0

if abs(N - M) < 2:
    ans += fact(N, MOD) * fact(M, MOD) % MOD
    if N == M:
        ans *= 2
        ans %= MOD
print(ans)