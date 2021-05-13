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
mod = 10**9+7 #998244353
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    h,w = map(int,ipt().split())
    dq = deque()
    a = [input()+"#" for i in range(h)] + ["#"*(w+1)]
    d = [[-1]*(w+1) for i in range(h+1)]
    for i in range(h):
        d[i][w] = 0
    for i in range(w):
        d[h][i] = 0

    for i in range(h):
        ai = a[i]
        for j in range(w):
            if ai[j] == "#":
                d[i][j] = 0
                for dx,dy in dir:
                    nx = i+dx
                    ny = j+dy
                    if a[nx][ny] == "." and d[nx][ny] == -1:
                        dq.append((nx,ny))
                        d[nx][ny] = 1

    while dq:
        qx,qy = dq.popleft()
        nd = d[qx][qy]
        for dx,dy in dir:
            nx = qx+dx
            ny = qy+dy
            if a[nx][ny] == "." and d[nx][ny] == -1:
                dq.append((nx,ny))
                d[nx][ny] = nd+1

#    print(d)
    ma = 0
    for i in d:
        for j in i:
            if ma < j:
                ma = j

    print(ma)




    return None

if __name__ == '__main__':
    main()
