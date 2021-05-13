from fractions import gcd
from functools import reduce
import sys
import numpy as np

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def lcm(a, b):
    return a // gcd(a, b) * b


def lcm_list(S):
    return reduce(lcm, S)


# mod m におけるaの逆元
def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m

    # 負の場合は m を足して正の数にする
    if u < 0:
        u += m
    return u


def main():
    N = int(input())
    A = list(map(int, input().split()))
    L = lcm_list(A)
    L %= MOD
    ans = 0
    for a in A:
        a_ = modinv(a, MOD)
        ans += L * a_ % MOD
    ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
