S = int(input())


def cmb(n, r, p):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = 1
    for i in range(n, n - r, -1):
        over = over * i % p
    under = 1
    for i in range(1, r + 1):
        under = under * i % p
    inv = pow(under, p - 2, p)
    return over * inv % p


M = 10 ** 9 + 7
ans = 0
for i in range(1, S):
    if S - 3 * i < 0:
        break
    ans += cmb(S - 3 * i + i - 1, i - 1, M)
    ans %= M
print(ans)
