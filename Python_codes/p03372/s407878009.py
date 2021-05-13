import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,c = map(int,ipt().split())
    stt = [tuple(map(int,ipt().split())) for _ in range(n)]

    rw = [0]*(n+1)
    rh = [0]*(n+1)
    lw = [0]*(n+1)
    lh = [0]*(n+1)
    nr = 0
    for i,si in enumerate(stt):
        nr += si[1]
        rw[i+1] = nr-si[0]*2 if rw[i]<nr-si[0]*2 else rw[i]
        rh[i+1] = nr-si[0] if rh[i]<nr-si[0] else rh[i]
    nl = 0
    for i,si in enumerate(stt[::-1]):
        nl += si[1]
        lw[i+1] = nl-(c-si[0])*2 if lw[i]<nl-(c-si[0])*2 else lw[i]
        lh[i+1] = nl-(c-si[0]) if lh[i]<nl-(c-si[0]) else lh[i]

    ma = 0
    for i in range(n):
        if ma < rw[i]+lh[n-i]:
            ma = rw[i]+lh[n-i]
        if ma < lw[i]+rh[n-i]:
            ma = lw[i]+rh[n-i]
    print(ma)
    return

if __name__ == '__main__':
    main()
