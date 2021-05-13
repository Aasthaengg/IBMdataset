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
    n = int(ipt())
    jobs = []
    for i in range(n):
        a,b = map(int,ipt().split())
        jobs.append((b,a))
    jobs.sort()
    t = 0
    for bi,ai in jobs:
        t += ai
        if bi < t:
            print("No")
            exit()

    print("Yes")
    return None

if __name__ == '__main__':
    main()
