N, M = map(int, input().split())
mod = 10 ** 9 + 7


def prime_factorization(n):  # 素因数分解
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            res.append((i, cnt))
    if n > 1:
        res.append((n, 1))
    return res


def binomial_coefficient(n, r, mod=10**9+7):
    """
    二項係数nCr, (n,r)をmodで除したあまりを返す
    """
    res = 1
    div = 1
    r = min(r, n - r)
    for i in range(r):
        res *= (n - i) % mod
        div *= (i + 1) % mod
    res *= pow(div, mod - 2, mod)
    return res % mod


pf = prime_factorization(M)
ans = 1
for _, x in pf:
    ans = (ans * binomial_coefficient(N+x-1, x, mod)) % mod
print(ans)
