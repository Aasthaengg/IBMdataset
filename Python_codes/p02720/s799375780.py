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
    k = int(ipt())
    q = queue.Queue()
    for i in range(1,10):
        q.put(i)
    for _ in [0]*k:
        qi = q.get()
        if not qi%10 == 0:
            q.put(qi*10+qi%10-1)
        q.put(qi*10+qi%10)
        if not qi%10 == 9:
            q.put(qi*10+qi%10+1)
    print(qi)
    return

if __name__ == '__main__':
    main()
