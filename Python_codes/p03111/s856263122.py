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
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n,a,b,c = map(int,ipt().split())
    l = [int(ipt()) for i in range(n)]
    mi = 10**18

    for i in range(4**n):
        sa = 0
        sb = 0
        sc = 0
        na = 0
        nb = 0
        nc = 0
        for j in range(n):
            ni = i>>(2*j)
            if (ni&2):
                if ni&1:
                    sa += l[j]
                    na += 1
                else:
                    sb += l[j]
                    nb += 1
            elif ni&1:
                sc += l[j]
                nc += 1
        if na*nb*nc == 0:
            continue
        nm = abs(sa-a)+abs(sb-b)+abs(sc-c)+(na+nb+nc-3)*10
        if nm < mi:
            mi = nm

    print(mi)



    return None

if __name__ == '__main__':
    main()
