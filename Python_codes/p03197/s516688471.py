# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
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

def run():
    N, *A = map(int, read().split())
    dic = defaultdict(lambda:0)
    for a in A:
        dic[a] += 1
    G = {}

    for key in sorted(list(dic.keys())):
        G[N] = key
        N -= dic[key]

    criteria = 0
    for key in G.keys():
        if G[key] % 2:
            criteria ^= key

    if not criteria:
        print('second')
    else:
        print('first')
if __name__ == "__main__":
    run()
