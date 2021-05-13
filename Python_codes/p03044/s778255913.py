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
    n = int(ipt())
    way = [[] for i in range(n+1)]
    for i in range(n-1):
        u,v,w = map(int,ipt().split())
        way[u].append((v,w))
        way[v].append((u,w))

    col = [-1]*(n+1)
    q = [(1,0)]
    col[1] = 0
    while q:
        qi,ci = q.pop()
#        print(qi,ci)
        for j,lj in way[qi]:
            if col[j] == -1:
                cj = (ci+lj)%2
                col[j] = cj
                q.append((j,cj))

    for i in col[1::]:
        print(i)

    return None

if __name__ == '__main__':
    main()
