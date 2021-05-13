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
    b = []
    b0 = 0
    for i,ai in enumerate(a):
        if i%2 == 1:
            b0 -= ai
        else:
            b0 += ai
    b.append(b0)
    for i in range(n-1):
        b.append((a[i]-b[-1]//2)*2)

    print(" ".join(map(str,b)))


    return None

if __name__ == '__main__':
    main()
