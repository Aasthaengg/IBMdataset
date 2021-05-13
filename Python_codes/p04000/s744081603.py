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
    for i in range(n):
        a, b = list(map(int, input().rstrip('\n').split()))
        a -= 1
        b -= 1
        for j in range(max(1, a - 1), min(h-1, a + 2)):
            for k in range(max(1, b - 1), min(w-1, b + 2)):
                d[j, k] += 1
    ls = [0] * 10
    for k, v in sorted(d.items(), key=lambda x: x[1]):
        ls[v] += 1
    ls[0] = (h - 3 + 1) * (w - 3 + 1) - sum(ls)
    for i in range(10):
        print(ls[i])


if __name__ == '__main__':
    slove()
