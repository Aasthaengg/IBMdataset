import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n = int(ipt())
    l = []
    if n%2 == 0:
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if i == j or i+j == n+1:
                    continue
                else:
                    l.append((i,j))
    else:
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if i+j == n:
                    continue
                else:
                    l.append((i,j))
    print(len(l))
    for i,j in l:
        print(i,j)
    return

if __name__ == '__main__':
    main()
