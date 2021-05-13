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
    way = [[] for _ in [0]*n]
    for i in [0]*(n-1):
        a,b = map(int,ipt().split())
        way[a-1].append(b-1)
        way[b-1].append(a-1)
    c = [int(i) for i in ipt().split()]
    c.sort(reverse=True)
    ans = [0]*n
    q = queue.Queue()
    ans[0] = c[0]
    ni = 1
    q.put(0)
    sum = 0
    while ni < n:
        qi = q.get()
        for i in way[qi]:
            if ans[i] == 0:
                ans[i] = c[ni]
                sum += c[ni]
                ni += 1
                q.put(i)

    print(sum)
    print(" ".join(map(str,ans)))



    return

if __name__ == '__main__':
    main()
