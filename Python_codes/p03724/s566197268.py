import math
import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,m = map(int,ipt().split())
    ts = np.zeros(n+1,dtype=int)
    for _ in range(m):
        a,b = map(int,ipt().split())
        ts[a] += 1
        ts[b] += 1
    if np.count_nonzero(ts%2) == 0:
        print("YES")
    else:
        print("NO")
    return

if __name__ == '__main__':
    main()
