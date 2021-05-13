'''
研究室PCでの解答
'''
import math
#import numpy as np
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7

def main():
    n = int(ipt())
    a = [int(i) for i in ipt().split()]
    nm = 0
    sm = 0
    p = 1
    for i in a:
        ns = sm+i
        if p:
            if ns <= 0:
                nm += 1-ns
                sm = 1
            else:
                sm = ns
        else:
            if ns >= 0:
                nm += 1+ns
                sm = -1
            else:
                sm = ns
        p = 1-p
    mi = nm
    nm = 0
    sm = 0
    p = 0
    for i in a:
        ns = sm+i
        if p:
            if ns <= 0:
                nm += 1-ns
                sm = 1
            else:
                sm = ns
        else:
            if ns >= 0:
                nm += 1+ns
                sm = -1
            else:
                sm = ns
        p = 1-p

    print(min(nm,mi))

    return None

if __name__ == '__main__':
    main()
