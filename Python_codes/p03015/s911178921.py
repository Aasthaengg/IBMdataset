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
    l = input()
    n = len(l)

    dp_small = [0] * n
    dp_indet = [0] * n

    dp_small[0] = 1
    dp_indet[0] = 2

    for i in range(1,n):
        bit = l[i]

        if bit == "1":
            dp_small[i] += dp_small[i-1] * 3 + dp_indet[i-1]
            dp_indet[i] += 2 * dp_indet[i-1]
        else:
            dp_small[i] += dp_small[i-1] * 3
            dp_indet[i] += dp_indet[i-1]

        dp_small[i] %= MOD
        dp_indet[i] %= MOD

    print((dp_small[-1]+dp_indet[-1])% MOD)


if __name__ == '__main__':
    main()
