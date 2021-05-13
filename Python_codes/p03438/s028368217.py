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


class PriorityQueue:
    def __init__(self, l=[]):
        self.q = l
        heapq.heapify(self.q)
        return

    def push(self, n):
        heapq.heappush(self.q, n)
        return

    def pop(self):
        return heapq.heappop(self.q)


MOD = int(1e09) + 7
INF = int(1e15)


def main():
    # sys.stdin = open("sample.txt")
    n = Scanner.int()
    A = Scanner.map_int()
    B = Scanner.map_int()
    cnt = 0
    for i in range(n):
        if A[i] < B[i]:
            cnt += (B[i] - A[i]) // 2
        else:
            cnt -= (A[i] - B[i])
    print('NYoe s'[cnt >= 0::2])
    return


if __name__ == "__main__":
    main()
