# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7

def mapline(t = int):
    return map(t, sysread().split())
def mapread(t = int):
    return map(t, read().split())


def run():
    N, M = mapline()
    cache = {}
    for i in range(M):
        a, b = mapline()
        cache[a] = cache.get(a, 0) + 1
        cache[b] = cache.get(b, 0) + 1

    for key in cache.keys():
        if cache[key] % 2:
            print('NO')
            return

    print('YES')
    return

if __name__ == "__main__":
    run()
