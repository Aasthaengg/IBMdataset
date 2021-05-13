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
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    m,k = map(int,ipt().split())
    if m == 1:
        if k == 0:
            print("0 1 1 0")
        else:
            print(-1)
        exit()
    if k <= 2**m-1:
        a = []
        b = []
        for i in range(m):
            if (k>>i)&1:
                a.append(2**i)
        sa = set(a)
        for i in range(2**m):
            if not i in sa:
                b.append(i)
        print(" ".join(map(str,a+b+a[::-1]+b[::-1])))
    else:
        print(-1)

    return None

if __name__ == '__main__':
    main()
