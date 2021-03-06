import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

mod = 10**9+7

n,a,b = map(int, input().split())

# def comb(n, k):
#     c = 1
#     for i in range(n - k + 1, n + 1):
#         c *= i
#         c %= mod
#
#     for i in range(1, k + 1):
#         c *= pow(i, mod - 2, mod)
#         c %= mod
#
#     return c

def comb(n, k):
    c = 1
    for i in range(k):
        c *= n - i
        c %= mod

    d = 1
    for i in range(1, k + 1):
        d *= i
        d %= mod

    return (c * pow(d, mod - 2, mod)) % mod

ans = pow(2, n, mod) - 1 - comb(n, a) - comb(n, b)
print(ans % mod)
