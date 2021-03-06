# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque

def prime_factorization(x):
    """素因数分解"""
    import math
    re = []
    i = 2
    while x != 1:
        if x % i == 0:
            re.append(i)
            x //= i
        else:
            i += 1
            if i > math.sqrt(x):
                re.append(x)
                break
    return re


def cmb(n, r):
    """組み合わせ"""
    import math
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(N):
    pf = []
    for i in range(1, N + 1):
        pf += prime_factorization(i)
    pf_num = {}
    for p in pf:
        pf_num.setdefault(p, 0)
        pf_num[p] += 1
    over2 = 0
    over4 = 0
    over14 = 0
    over24 = 0
    over74 = 0
    for v in pf_num.values():
        if 74 <= v:
            over74 += 1
        if 24 <= v:
            over24 += 1
        if 14 <= v:
            over14 += 1
        if 4 <= v:
            over4 += 1
        if 2 <= v:
            over2 += 1
    ans = 0
    # 3-5-5
    ans += (over2 - over4) * cmb(over4, 2)
    ans += cmb(over4, 3) * 3

    # 5-15
    ans += (over4 - over14) * over14
    ans += cmb(over14, 2) * 2

    # 3-25
    ans += (over2 - over24) * over24
    ans += cmb(over24, 2) * 2

    # 75
    ans += over74

    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
