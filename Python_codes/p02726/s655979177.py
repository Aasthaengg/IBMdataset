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
from collections import deque
from functools import lru_cache
import bisect
import re
import queue
import decimal


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
        return [Scanner.string() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [Scanner.int() for i in range(n)]


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
    def divisor(n):
        res = []
        i = 1
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
        return res

    @staticmethod
    def round_up(a, b):
        return -(-a // b)

    @staticmethod
    def is_prime(n):
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

    @staticmethod
    def fact(N):
        res = {}
        tmp = N
        for i in range(2, int(N ** 0.5 + 1) + 1):
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            if cnt > 0:
                res[i] = cnt
        if tmp != 1:
            res[tmp] = 1
        if res == {}:
            res[N] = 1
        return res


def pop_count(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


MOD = int(1e09) + 7
INF = int(1e15)


def dist(i, j, X, Y):
    if j <= X:
        return j - i
    if i >= Y:
        return j - i
    if i <= X < Y <= j:
        return X - i + 1 + j - Y
    if X <= i < j <= Y:
        d1 = j - i
        d2 = i - X + 1 + Y - j
        return min(d1, d2)
    if i <= X <= j <= Y:
        d1 = j - i
        d2 = X - i + 1 + Y - j
        return min(d1, d2)
    else:
        d1 = j - i
        d2 = i - X + 1 + j - Y
        return min(d1, d2)


def solve():
    N, X, Y = Scanner.map_int()
    ans = [0 for _ in range(1, N + 1)]
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            d = dist(i, j, X, Y)
            ans[d] += 1

    print(*ans[1:], sep='\n')


def main():
    # sys.stdin = open("sample.txt")
    # T = Scanner.int()
    # for _ in range(T):
    #     solve()
    # print('YNeos'[not solve()::2])
    solve()


if __name__ == "__main__":
    main()
