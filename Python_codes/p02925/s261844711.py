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

def main():
    n = int(ipt())
    a = [[]]
    for i in range(n):
        a.append([int(i) for i in ipt().split()])
    ta = [1]*(n+1)
    ht = [[0]*(n+1) for i in range(n+1)]
    ng = []
    for i in range(1,n+1):
        ai = min(i,a[i][0])
        bi = max(i,a[i][0])
        if ht[ai][bi]:
            ng.append((ai,bi))
        ht[ai][bi] += 1
    t = 0
    d = 0
    while ng:
#        print(ng,ht)
        pg = []
        for ag,bg in ng:
            tag = ta[ag]
            if tag != n-1:
                aai = min(ag,a[ag][tag])
                abi = max(ag,a[ag][tag])
                if ht[aai][abi]:
                    pg.append((aai,abi))
                ht[aai][abi] += 1
                ta[ag] += 1
            tbg = ta[bg]
            if tbg != n-1:
                bai = min(bg,a[bg][tbg])
                bbi = max(bg,a[bg][tbg])
                if ht[bai][bbi]:
                    pg.append((bai,bbi))
                ht[bai][bbi] += 1
                ta[bg] += 1
            t += 1
        d += 1
        ng = pg*1

    if t == n*(n-1)//2:
        print(d)
    else:
        print(-1)



    return None

if __name__ == '__main__':
    main()
