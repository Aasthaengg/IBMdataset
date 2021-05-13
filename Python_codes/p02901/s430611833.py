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
    dp = [10**10 for _ in [0]*(2**n)]
    dp[0] = 0
    for _ in range(m):
        a,b = map(int,ipt().split())
        c = [int(i) for i in ipt().split()]
        opn = 0
        for i in c:
            opn += 2**(i-1)
        for i in range(2**n):
            if i&opn == 0:
                continue
            elif dp[i] > dp[i-(i&opn)]+a:
                dp[i] = dp[i-(i&opn)]+a

    if dp[2**n-1] >= 10**10:
        print(-1)
    else:
        print(dp[2**n-1])
    return

if __name__ == '__main__':
    main()
