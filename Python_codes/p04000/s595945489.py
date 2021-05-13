import sys
import bisect
import collections
import fractions
import heapq
import math
from operator import mul
from functools import reduce
from functools import lru_cache


def slove():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    h, w, n = list(map(int, input().rstrip('\n').split()))
    d = collections.defaultdict(int)
    dt = collections.defaultdict(int)
    for i in range(n):
        a, b = list(map(int, input().rstrip('\n').split()))
        a -= 1
        b -= 1
        for j in range(max(1, a - 1), min(h-1, a + 2)):
            for k in range(max(1, b - 1), min(w-1, b + 2)):
                d[j, k] += 1
                dt[d[j, k]] += 1
                dt[d[j, k]-1] -= 1
    dt[0] += (h - 3 + 1) * (w - 3 + 1)
    for i in range(10):
        print(dt[i])


if __name__ == '__main__':
    slove()
