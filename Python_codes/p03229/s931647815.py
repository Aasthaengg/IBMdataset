#!/usr/bin/env python3
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def sum_of_arithmetic_progression(s, d, n):
    return n * (2 * s + (n - 1) * d) // 2


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return a / g * b


def func1(A):
    ans = 0
    N = len(A)
    m, p = [], []
    for i in range(N):
        if i < N // 2:
            m.append(A[i])
        else:
            p.append(A[i])

    ans -= sum(m) * 2
    ans += sum(p) * 2

    if N % 2 == 0:
        ans += m[-1]
        ans -= p[0]
    else:
        ans -= p[0]
        ans -= p[1]

    return ans


def func2(A):
    ans = 0
    N = len(A)
    m, p = [], []
    for i in range(N):
        if i < N // 2 + 1:
            m.append(A[i])
        else:
            p.append(A[i])

    ans -= sum(m) * 2
    ans += sum(p) * 2

    if N % 2 == 0:
        ans += m[-1]
        ans -= p[0]
    else:
        ans += m[-1]
        ans += m[-2]

    return ans


def solve(A):
    return max(func1(A[:]), func2(A[:]))


def check(A):
    ans = 0
    for p in permutations(A):
        tmp = 0
        for i in range(1, len(p)):
            tmp += abs(p[i] - p[i - 1])

        ans = max(ans, tmp)
    return ans


def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    A.sort()

    if N < 5:
        print(check(A))
    else:
        print(solve(A))


if __name__ == '__main__':
    main()