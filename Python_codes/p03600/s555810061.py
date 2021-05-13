'''
自宅用PCでの解答
'''
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
mod = 10**9+7
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n = int(ipt())
    a = [[int(i) for i in ipt().split()] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[j][k] > a[j][i]+a[i][k]:
                    print(-1)
                    exit()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[j][i] != 0 and a[i][k] != 0 and a[j][k] == a[j][i]+a[i][k]:
                    a[j][k] = 0

    ans = 0
    for i in range(n):
        for j in range(i,n):
            ans += a[i][j]

    print(ans)

    return None

if __name__ == '__main__':
    main()
