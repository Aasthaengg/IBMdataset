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


def main():
    # sys.stdin = open("sample.txt")
    N = Scanner.int()
    A = Scanner.map_int()
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - (i+1)
    B.sort()

    a, b = B[N//2-1], B[N//2]
    ans = 0
    tmp = 0
    for i in range(N):
        ans += abs(A[i] - (a + i + 1))
        tmp += abs(A[i] - (b + i + 1))
    ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
