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
    n,m = map(int,ipt().split())
    way = [[] for _ in [0]*n]
    for i in range(m):
        a,b = map(int,ipt().split())
        way[a-1].append((b-1,i))
        way[b-1].append((a-1,i))
    ans = 0
    q = queue.Queue()
    for i in range(m):
        al = [-1 for i in range(n)]
        q.put(0)
        al[0] = 0
        while not q.empty():
            qi = q.get()
            for j,wn in way[qi]:
                if wn == i or al[j] == 0:
                    continue
                else:
                    al[j] = 0
                    q.put(j)
        if -1 in al:
            ans += 1

    print(ans)

    return

if __name__ == '__main__':
    main()
