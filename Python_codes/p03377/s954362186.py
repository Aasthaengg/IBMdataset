import math, sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import lru_cache
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, permutations
input = sys.stdin.readline
mod = 10**9 + 7
ns = lambda: input().strip()
ni = lambda: int(input().strip())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

def main():
    a, b, x = nm()

    if x <= a + b and x >= a:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()