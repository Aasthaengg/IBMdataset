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
    dx = dict()
    dy = dict()
    xs = []
    ys = []
    for _ in range(n):
        x,y = map(int,ipt().split())
        dx[x] = y
        dy[y] = x
        xs.append(x)
        ys.append(y)
    xs.sort()
    ys.sort()
    sm = [[0]*(n+1) for i in range(n+1)]
    f = False
    ly = dx[xs[n-1]]
    for i,yi in enumerate(ys[::]):
        if f:
            sm[n-1][i] = 0
        else:
            sm[n-1][i] = 1
        if ly == yi:
            f = True
    for i,xi in enumerate(xs[n-2::-1]):
        f = False
        smx = sm[n-i-2]
        smpx = sm[n-i-1]
        ly = dx[xi]
        for j,yj in enumerate(ys):
            if f:
                smx[j] = smpx[j]
            else:
                smx[j] = smpx[j]+1
            if ly == yj:
                f = True
    ma = 4*10**18+1
    for xl,xli in enumerate(xs[:n-1:]):
        smxl = sm[xl]
        for xr,xri in enumerate(xs[xl+1::]):
            smxr = sm[xl+xr+2]
            for yd,ydi in enumerate(ys[:n-1:]):
                for yu,yui in enumerate(ys[yd+1::]):
                    sk = smxl[yd]+smxr[yu+yd+2]-smxl[yu+yd+2]-smxr[yd]
                    if sk == k:
                        ss = (yui-ydi)*(xri-xli)
                        if ss < ma:
                            ma = ss
    print(ma)

    return

if __name__ == '__main__':
    main()
