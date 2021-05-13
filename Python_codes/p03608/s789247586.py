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
    n,m,r = map(int,ipt().split())
    tgt = [int(i)-1 for i in ipt().split()]
    dt = [[10**18]*n for i in range(n)]
    for i in range(n):
        dt[i][i] = 0
    for i in range(m):
        a,b,c = map(int,ipt().split())
        a -= 1
        b -= 1
        dt[a][b] = c
        dt[b][a] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dt[j][k] > dt[j][i]+dt[i][k]:
                    dt[j][k] = dt[j][i]+dt[i][k]

    mi = 10**18
    for i in itertools.permutations(range(r)):
        nm = 0
        for j in range(r-1):
            nm += dt[tgt[i[j]]][tgt[i[j+1]]]
        if mi > nm:
            mi = nm

    print(mi)

    return None

if __name__ == '__main__':
    main()
