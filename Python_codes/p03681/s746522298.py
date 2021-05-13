n, m = map(int, input().split())
MOD = 1000000007
def nPk(n, k):
    r = 1
    while k > 0:
        r *= n
        r %= MOD
        n -= 1
        k -= 1
    return r
if abs(n - m) > 1:
    print(0)
elif n == m:
    print(nPk(n, n) * nPk(m, m) * 2 % MOD)
else:
    print(nPk(n, n) * nPk(m, m) % MOD)