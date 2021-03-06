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



def solve():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    p = 0
    q = 0
    for i, v in enumerate(permutations(range(1, N + 1)), start=1):
        p_ok = True
        q_ok = True
        for j in range(N):
            p_ok &= v[j] == P[j]
            q_ok &= v[j] == Q[j]

        if p_ok:
            p = i
        if q_ok:
            q = i

    print(abs(p - q))


def main():
    solve()


if __name__ == '__main__':
    main()
