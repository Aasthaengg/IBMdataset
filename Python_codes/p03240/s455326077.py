# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
#from collections import defaultdict
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
    N = int(sysread())
    V = []
    x0, y0, h0 = None, None, None
    for _ in range(N):
        x,y,h = mapline()
        if h > 0 and x0 == None:
            x0, y0, h0 = x,y,h
        V.append((x, y, h))

    for x in range(0, 101):
        for y in range(0, 101):
            H = h0 + abs(x0-x) + abs(y0-y)
            done = True
            for xk, yk, hk in V:
                h_ = max(H - abs(xk-x) - abs(yk-y), 0)
                if h_ != hk:
                    done = False
                    break
            if done:
                print(f'{x} {y} {H}')
                return


if __name__ == "__main__":
    run()
