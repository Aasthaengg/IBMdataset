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
import re


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
INF = int(1e15)

T_MAX = int(1e05) + 1


def main():
    # sys.stdin = open("sample.txt")
    N, C = Scanner.map_int()
    S = [Scanner.map_int() for _ in range(N)]
    M = [[0 for _ in range(C)] for _ in range(T_MAX)]
    for i in range(N):
        M[S[i][0]-1][S[i][2]-1] += 1
        M[S[i][1]][S[i][2]-1] -= 1
    for c in range(C):
        for t in range(1, T_MAX):
            M[t][c] += M[t-1][c]
    ans = 0
    for t in range(T_MAX):
        ans = max(ans, M[t].count(1))
    print(ans)


if __name__ == "__main__":
    main()
