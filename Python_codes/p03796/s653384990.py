import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    n = int(input())
    mod = 10**9+7

    ans = 1
    for i in range(n):
        ans *= i+1
        ans %= mod
    print(ans)


if __name__ == '__main__':
    main()
