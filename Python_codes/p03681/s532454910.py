def kaijou(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
        ret %= MOD
    return ret


n, m = map(int, input().split())
MOD = 10**9 + 7

if abs(n - m) >= 2:
    print(0)
else:
    if n == m:
        ans = kaijou(n)**2 * 2 % MOD
    else:
        n, m = max(n, m), min(n, m)
        ans = kaijou(n) * kaijou(m) % MOD
    print(ans)
