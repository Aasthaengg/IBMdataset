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
    n,m = map(int,ipt().split())
    way = [[] for i in range(n+1)]
    for i in range(m):
        l,r,d = map(int,ipt().split())
        way[l].append((r,d))
        way[r].append((l,-d))
    q = []

    pl = [10**18]*(n+1)
    for i in range(1,n+1):
        if pl[i] != 10**18:
            continue
        q.append(i)
        pl[i] = 0
        while q:
            qi = q.pop()
            pq = pl[qi]
            for j,dj in way[qi]:
                if pl[j] == 10**18:
                    pl[j] = pq+dj
                    q.append(j)
                elif pl[j] != pq+dj:
                    print("No")
                    exit()
    print("Yes")

    return None

if __name__ == '__main__':
    main()
