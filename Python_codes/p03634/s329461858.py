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
    way = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c = map(int,ipt().split())
        way[a].append((b,c))
        way[b].append((a,c))
    q,k = map(int,ipt().split())
    l = [-1]*(n+1)
    l[k] = 0
    Q = queue.Queue()
    Q.put(k)
    while not Q.empty():
        qi = Q.get()
        lq = l[qi]
        for bi,ci in way[qi]:
            if l[bi] == -1:
                l[bi] = lq+ci
                Q.put(bi)

    for i in range(q):
        x,y = map(int,ipt().split())
        print(l[x]+l[y])

    return

if __name__ == '__main__':
    main()
