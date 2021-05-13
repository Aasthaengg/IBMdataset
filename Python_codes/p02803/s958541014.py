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

H, W = (None, None)
S = None


def bfs(h, w):
    if S[h][w] == '#':
        return 0
    q = queue.Queue()
    q.put((w, h))
    steps = [[-1 for _ in range(W)]for _ in range(H)]
    steps[h][w] = 0
    while not q.empty():
        p = q.get()
        DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for d in DIR:
            n = (p[0] + d[0], p[1] + d[1])
            if not (0 <= n[0] < W and 0 <= n[1] < H):
                continue
            if steps[n[1]][n[0]] != -1:
                continue
            if S[n[1]][n[0]] == '#':
                continue
            steps[n[1]][n[0]] = steps[p[1]][p[0]] + 1
            q.put(n)
    res = 0
    for s in steps:
        res = max(res, max(s))
    return res


def solve():
    global H, W, S
    H, W = Scanner.map_int()
    S = Scanner.string_list(H)
    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, bfs(h, w))
    print(ans)


def main():
    # sys.stdin = open("sample.txt")
    # T = Scanner.int()
    # for _ in range(T):
    #     solve()
    # print('YNeos'[not solve()::2])
    solve()


if __name__ == "__main__":
    main()
