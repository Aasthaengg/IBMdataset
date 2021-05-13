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
    a = [int(i) for i in ipt().split()]
    d = defaultdict(int)
    sm = 0
    d[0] += 1
    for ai in a:
        sm = (sm+ai)%m
        d[sm] += 1
    ans = 0
    for i in d.values():
        ans += i*(i-1)//2
    print(ans)


    return

if __name__ == '__main__':
    main()
