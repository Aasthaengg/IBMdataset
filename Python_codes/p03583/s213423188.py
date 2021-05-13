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

def main():
    N = int(ipt())
    for h in range(1,3501):
        for n in range(1,3501):
            k = 4*n*h-N*n-N*h
            if k <= 0:
                continue
            if n*h*N%k == 0 and 0<n*h*N//k:
                print(h,n,n*h*N//k)
                exit()

    return None

if __name__ == '__main__':
    main()
