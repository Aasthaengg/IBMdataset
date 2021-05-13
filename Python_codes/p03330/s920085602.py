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
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n,c = map(int,ipt().split())
    d = [[int(i) for i in ipt().split()] for j in range(c)]
    cs = [[int(i) for i in ipt().split()] for j in range(n)]
    di = [defaultdict(int) for i in range(3)]
    for i in range(n):
        for j in range(n):
            di[(i+j)%3][cs[i][j]] += 1

    cost = [[0]*c for i in range(3)]
    for i in range(3):
        for j in range(c):
            sm = 0
            for k in range(c):
                sm += d[k][j]*di[i][k+1]
            cost[i][j] = sm

    cm = [[(ci,i) for i,ci in enumerate(cost[j])] for j in range(3)]
    cm[0].sort()
    cm[1].sort()
    cm[2].sort()
    mi = 10**18
    for i in range(3):
        for j in range(3):
            for k in range(3):
                nm = cm[0][i][0]+cm[1][j][0]+cm[2][k][0]
                if cm[0][i][1] != cm[1][j][1] != cm[2][k][1] != cm[0][i][1] and mi > nm:
                    mi = nm

    print(mi)


    return None

if __name__ == '__main__':
    main()
