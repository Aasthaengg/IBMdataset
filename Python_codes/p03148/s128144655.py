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
    n,k = map(int,ipt().split())
    mat = [-1]*n
    susis = []
    smo = 0
    knds = 0
    for _ in range(n):
        t,d = map(int,ipt().split())
        t -= 1
        if mat[t] < d:
            mat[t] = d
        susis.append((d,t))
    susis.sort(reverse=True)
    kh = []
    res = []
    for i in range(k):
        di,ti = susis[i]
        smo += di
        if di == mat[ti]:
            mat[ti] = -1
            knds += 1
        else:
            hpq.heappush(res,di)
    for i in mat:
        if i != -1:
            hpq.heappush(kh,-i)

    ma = smo + knds**2
    while len(res) and len(kh):
        knds += 1
        smo -= hpq.heappop(res)
        smo -= hpq.heappop(kh)
        if ma < smo+knds**2:
            ma = smo+knds**2

    print(ma)


    return

if __name__ == '__main__':
    main()
