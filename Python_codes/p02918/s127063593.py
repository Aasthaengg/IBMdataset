# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7

def run():
    N, K = map(int, sysread().split())
    S = input()
    c = S[0]
    checkpoints = 0
    endpoints = 0
    for s in S:
        if c == 'L':
            if s == 'R':
                c = 'R'
                endpoints += 1
            else:
                continue
        elif c == 'R':
            if s == 'L':
                checkpoints += 1
                c = 'L'
            else:
                continue
    #print(checkpoints, endpoints)
    ans = N - 2 * checkpoints
    halfpoint = 0
    edge = 0
    if S[0] == 'R':
        edge += 1
    else:
        halfpoint += 1

    if S[-1] == 'L':
        edge += 1
    else:
        halfpoint += 1

    ans -= halfpoint
    val = min([checkpoints, endpoints, K])
    checkpoints -= val
    endpoints -= val
    K -= val
    ans += 2 * val

    if K > 0:
        if checkpoints > 0:
            if edge > 0:
                val = min([edge, checkpoints, K])
                K -= val
                edge -= K
                checkpoints -= K
                ans += val
    if K > 0:
        if halfpoint > 0 and endpoints > 0:
            val = min([K, halfpoint, endpoints])
            K -= val
            halfpoint -= val
            endpoints -= val
            ans += val

    print(ans)

if __name__ == "__main__":
    run()
