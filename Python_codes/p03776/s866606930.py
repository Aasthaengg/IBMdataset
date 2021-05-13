# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import string
import heapq
import _collections
from collections import Counter
from collections import defaultdict
from functools import lru_cache
import bisect


class Scanner():
    @staticmethod
    def int():
        return int(sys.stdin.readline().rstrip())

    @staticmethod
    def string():
        return sys.stdin.readline().rstrip()

    @staticmethod
    def map_int():
        return [int(x) for x in Scanner.string().split()]

    @staticmethod
    def string_list(n):
        return [input() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [int(input()) for i in range(n)]


class Math():
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return Math.gcd(b, a % b)

    @staticmethod
    def lcm(a, b):
        return (a * b) // Math.gcd(a, b)

    @staticmethod
    def roundUp(a, b):
        return -(-a // b)

    @staticmethod
    def toUpperMultiple(a, x):
        return Math.roundUp(a, x) * x

    @staticmethod
    def toLowerMultiple(a, x):
        return (a // x) * x

    @staticmethod
    def nearPow2(n):
        if n <= 0:
            return 0
        if n & (n - 1) == 0:
            return n
        ret = 1
        while(n > 0):
            ret <<= 1
            n >>= 1
        return ret

    @staticmethod
    def sign(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        return 1

    @staticmethod
    def isPrime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = int(n ** 0.5) + 1
        for i in range(3, d + 1, 2):
            if n % i == 0:
                return False
        return True


MOD = int(1e09) + 7
INF = int(1e09)

nCr = {}

sys.setrecursionlimit(100000)


def comb(n, r):
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    if (n, r) in nCr:
        return nCr[(n, r)]
    nCr[(n, r)] = comb(n-1, r) + comb(n-1, r-1)
    return nCr[(n, r)]


def main():
    # sys.stdin = open("sample.txt")
    N, A, B = Scanner.map_int()
    V = Scanner.map_int()
    V.sort(reverse=True)
    ans = 0
    for i in range(A):
        ans += V[i]
    ans /= A
    print(ans)

    vmin = V[A-1]
    if V[0] != V[A-1]:
        cnt = V.count(vmin)
        c = V[:A].count(vmin)
        print(comb(cnt, c))
        return

    c = V.count(vmin)
    cnt = 0
    for i in range(A, B+1):
        if V[i-1] != vmin:
            break
        cnt += comb(c, i)
    print(cnt)


if __name__ == "__main__":
    main()
