from collections import Counter


def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)


def combination(n, r, mod=10**9+7):
    """
    nCr mod m
    """
    if n < r:
        return 0
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res


n, p = map(int, input().split())
a = list(map(int, input().split()))
b = [ai % 2 for ai in a]
c = Counter(b)

ans = 0
if p == 0:
    even = (2 ** c[0])
    odd = 1
    for i in range(2, c[1] + 1, 2):
        odd += combination(c[1], i)
    ans = even * odd
else:
    even = (2 ** c[0])
    odd = 0
    for i in range(1, c[1] + 1, 2):
        odd += combination(c[1], i)
    ans = even * odd

print(ans)