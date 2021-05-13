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
    n,q = map(int,ipt().split())
    way = [[] for i in range(n+1)]
    for i in range(n-1):
        a,b = map(int,ipt().split())
        way[a].append(b)
        way[b].append(a)
    pl = [0]*(n+1)
    for i in range(q):
        p,x = map(int,ipt().split())
        pl[p] += x
    ans = [-1]*(n+1)
    ans[0] = 0
    ans[1] = pl[1]
    q = [(1,0)]
 
    while q:
        qi,qp = q.pop()
        qa = ans[qi]
        for j in way[qi]:
            if j == qp:
                continue
            ans[j] = qa+pl[j]
            q.append((j,qi))
 
    print(" ".join(map(str,ans[1::])))
 
    return None
 
if __name__ == '__main__':
    main()