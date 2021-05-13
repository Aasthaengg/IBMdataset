import sys

import bisect

# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd

# import itertools

# from operator import attrgetter, itemgetter
# import math

# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())

    ans = ""
    while abs(n) > 1:
        if n % 2 == 0:
            ans += "0"
            n //= 2
            n *= -1
        else:
            ans += "1"
            n //= 2
            n *= -1

    if n == -1:
        ans += "11"
    else:
        ans += str(n)

    ans = ans[::-1]
    print(ans)


if __name__ == '__main__':
    main()
