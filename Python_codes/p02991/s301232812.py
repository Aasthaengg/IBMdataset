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
    n,m = map(int,ipt().split())
    way = [[] for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,ipt().split())
        way[u].append(v)
    dist = [[-1]*3 for _ in range(n+1)]
    s,t = map(int,ipt().split())
    dist[s][0] = 0
    q = queue.Queue()
    q.put((s,0))
    while not q.empty():
        pi,pd = q.get()
        for i in way[pi]:
            if dist[i][(pd+1)%3] == -1:
                dist[i][(pd+1)%3] = (pd+1)//3
                q.put((i,pd+1))
    print(dist[t][0])

    return

if __name__ == '__main__':
    main()
