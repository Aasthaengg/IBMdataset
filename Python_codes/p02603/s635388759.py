'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
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
    yt = []
    p = 1
    nk = 1000
    kb = 0
    for i,na in enumerate(a[1::]):
        ai = a[i]
        if p:
            if ai < na:
                p = 0
                kb = nk//ai
                nk %= ai
        else:
            if ai > na:
                p = 1
                nk += kb*ai
                kb = 0

    print(nk+kb*a[-1])
    return None

if __name__ == '__main__':
    main()
