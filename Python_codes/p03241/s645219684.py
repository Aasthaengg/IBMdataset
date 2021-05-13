from math import gcd

def solve():
    n, m = map(int, input().split())
    d = m // n
    p = m % n
    res = max(1, gcd(d, d + p))
    if p == 0:
        print(res)
        exit()
    while d > res:
        d -= 1
        p += n
        if p % d == 0:
            res = max(res, d)
    print(res)


solve()
