# import bisect
# from collections import Counter, defaultdict, deque, namedtuple
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
    k, a, b = list(map(int,ipti().split()))

    viscuit = 1

    #aをbにするとき増える枚数
    a2b = b - a

    #最初は1枚持っている

    if k >= (a-1):
        k -= (a-1)
        viscuit += (a-1)
    else:
        viscuit += k
        k = 0

    if a2b > 2:
        times = k // 2
        rem = k % 2
        viscuit += a2b * times
        viscuit += rem
    else:
        viscuit += k
        k = 0

    print(viscuit)


if __name__ == '__main__':
    main()