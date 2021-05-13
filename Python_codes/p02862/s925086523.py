# 20-7-30 再トライ
import sys

def binomial_p(n, k, p):
    k = min(k, n - k)
    if k == 0: return 1
    numer = 1
    denom = 1
    for i in range(k):
        numer = numer * (n - i) % p
        denom = denom * (k - i) % p
    return numer * pow(denom, p - 2, p) % p


X, Y = [int(x) for x in input().split()]
p = 10 ** 9 + 7

if (2 * X - Y) % 3 != 0 or (2 * Y - X) % 3 != 0 or\
    2 * X - Y < 0 or 2 * Y - X < 0:
    print(0)
    sys.exit()

m = (2 * X - Y) // 3
n = (2 * Y - X) // 3
print(binomial_p(m + n, m, p))