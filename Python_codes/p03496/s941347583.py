#!/usr/bin/python3

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


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def main():
    N = int(input())
    A = list(map(int, input().split()))

    m, m_idx = abs(A[0]), 0
    for i, a in enumerate(A):
        if abs(a) > m:
            m = abs(a)
            m_idx = i

    ans = []
    for i in range(N):
        A[i] += A[m_idx]
        ans.append((m_idx + 1, i + 1))

    if A[m_idx] >= 0:
        for i in range(N - 1):
            ans.append((i + 1, i + 2))
    else:
        for i in range(N - 1, 0, -1):
            ans.append((i + 1, i - 1 + 1))

    print(len(ans))
    for x in ans:
        print(*x)


if __name__ == '__main__':
    main()
