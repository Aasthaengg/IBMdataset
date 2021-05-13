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
    s = input()
    t = input()
    g = math.gcd(n,m)
    l = n*m//g
    sg = n//g
    tg = m//g
    for i in range(g):
        if s[sg*i] != t[tg*i]:
            print(-1)
            exit()

    print(l)

    return

if __name__ == '__main__':
    main()
