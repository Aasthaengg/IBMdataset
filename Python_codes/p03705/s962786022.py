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
    n,a,b = map(int,ipt().split())
    if a > b:
        print(0)
    else:
        print(max(0,(n-2)*b-(n-2)*a+1))

    return

if __name__ == '__main__':
    main()
