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
import queue


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


class PriorityQueue:
    def __init__(self, l=[]):
        self.__q = l
        heapq.heapify(self.__q)
        return

    def push(self, n):
        heapq.heappush(self.__q, n)
        return

    def pop(self):
        return heapq.heappop(self.__q)


sys.setrecursionlimit(1000000)
MOD = int(1e09) + 7
INF = int(1e30)


def main():
    # sys.stdin = open("Sample.txt")
    N, C = Scanner.map_int()
    D = Scanner.int_list_list(C)
    colors = Scanner.int_list_list(N)
    for i in range(N):
        for j in range(N):
            colors[i][j] -= 1
    T = [[0 for _ in range(C)] for _ in range(3)]
    for h in range(N):
        for w in range(N):
            T[(h+w) % 3][colors[h][w]] += 1
    ans = INF
    for a in range(C):
        for b in range(C):
            for c in range(C):
                if a == b or a == c or b == c:
                    continue
                now = 0
                for d in range(C):
                    now += T[0][d] * D[d][a]
                    now += T[1][d] * D[d][b]
                    now += T[2][d] * D[d][c]
                ans = min(ans, now)
    print(ans)
    return


if __name__ == "__main__":
    main()
