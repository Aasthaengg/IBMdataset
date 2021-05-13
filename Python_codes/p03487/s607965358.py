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
    d = defaultdict(int)
    for a in ipt().split():
        d[int(a)] += 1

    ans = 0
    for dk,dv in d.items():
        if dk > dv:
            ans += dv
        elif dk < dv:
            ans += (dv-dk)
    print(ans)
    return

if __name__ == '__main__':
    main()
