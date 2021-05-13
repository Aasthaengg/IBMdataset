import sys

# import bisect
# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
import itertools
# from operator import attrgetter, itemgetter
# import math

# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, a, b, c = list(map(int, readline().split()))
    l = [int(input()) for _ in range(n)]

    ans = INF

    selects = list(itertools.product(range(4), repeat=n))

    for select in selects:
        mp = -30
        bamboo_length = [0] * 3
        for i, num in enumerate(select):
            if num != 3:
                bamboo_length[num] += l[i]
                mp += 10

        for length in bamboo_length:
            if length == 0:
                break
        else:
            mp += abs(a - bamboo_length[0])
            mp += abs(b - bamboo_length[1])
            mp += abs(c - bamboo_length[2])
            ans = min(mp, ans)

    print(ans)


if __name__ == '__main__':
    main()
