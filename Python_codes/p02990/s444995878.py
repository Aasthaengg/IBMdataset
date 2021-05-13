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
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7
def intread():
    return int(sysread())
def mapline(t = int):
    return map(t, sysread().split())
def mapread(t = int):
    return map(t, read().split())

def generate_inv(n,mod):
    """
    逆元行列
    n >= 2
    Note: mod must bwe a prime number
    """
    ret = [0, 1]
    for i in range(2,n+1):
        next = -ret[mod%i] * (mod // i)
        next %= mod
        ret.append(next)
    return ret

def run():
    N, K = mapline()
    inv = generate_inv(K, mod)
    cache1 = 1
    cache2 = 1
    for i in range(1, K+1):
        cache1 *= (N-K+1 - (i-1))
        cache1 %= mod
        cache1 *= inv[i]
        cache1 %= mod
        if i == 1:
            cache2 = 1
        else:
            cache2 *= K-1 - (i-2)
            if cache2 == 0:
                cache2 = 1
            else:
                cache2 %=mod
                cache2 *= inv[i-1]
                cache2 %= mod
        #print(cache1, cache2)
        print(cache1 * cache2 % mod)



if __name__ == "__main__":
    run()
