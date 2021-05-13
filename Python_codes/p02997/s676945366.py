# import bisect
# from collections import Counter, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, k = list(map(int, ipti().split()))

    k_lim = ((n - 2) * (n - 1)) // 2

    if k_lim < k:
        print(-1)
        sys.exit()

    m1 = n - 1
    m2 = k_lim - k

    print(m1 + m2)

    for i in range(2, n + 1):
        print(1, i)

    e1 = 2
    e2 = 3
    e_num = 0

    while e_num < m2:
        print(e1, e2)
        e_num += 1
        e2 += 1
        if e2 > n:
            e1 += 1
            e2 = e1 + 1



if __name__ == '__main__':
    main()
