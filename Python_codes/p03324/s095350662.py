from heapq import heappush, heappop
from itertools import permutations, accumulate, combinations
import math
import bisect
import numpy as np
from collections import defaultdict, deque
from operator import itemgetter
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
# MOD = 10 ** 9 + 7
# INF = float("inf")


def main():
    d, n = map(int, input().split())
    if d == 0:
        ans = n
        if n == 100:
            ans += 1
    else:
        ans = 100 ** d * n
        if d == 1 and n == 100:
            ans += 100
        elif d == 2 and n == 100:
            ans += 10000
    print(ans)


if __name__ == '__main__':
    main()