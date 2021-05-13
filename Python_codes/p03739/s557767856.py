# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect
import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8


def run():
    n, *A = map(int, read().split())
    v = 0
    acum = []
    for a in A:
        v += a
        acum.append(v)

    # greedy
    ans = INF
    for V in (-1, 1):
        cums = 0
        count = 0
        for a in acum:
            #print(a, '---------')
            V *= -1
            if (a + cums) * V > 0:
                continue
            else:
                update = abs(a + cums) + 1
                cums += (update) * V
                count += update
                #print(V, cums, count)
        ans = min(ans, count)
    print(ans)



if __name__ == "__main__":
    run()
