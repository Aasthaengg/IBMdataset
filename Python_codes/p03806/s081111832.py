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
    n,ma,mb = map(int,ipt().split())
    dp = [[10**18]*(n*10+1) for _ in [0]*(n*10+1)]
    dp[0][0] = 0
    for _ in range(n):
        a,b,c = map(int,ipt().split())
        for i in range(n*10+1-a):
            dpi = dp[n*10-i-a]
            dpni = dp[n*10-i]
            for j in range(n*10+1-b):
                if dpni[n*10-j] > dpi[n*10-j-b]+c:
                    dpni[n*10-j] = dpi[n*10-j-b]+c
    mi = 10**18
    for i in range(1,n*10//max(ma,mb)+1):
        m = dp[ma*i][mb*i]
        if m < mi:
            mi = m
    if mi == 10**18:
        print(-1)
    else:
        print(mi)
    return

if __name__ == '__main__':
    main()
