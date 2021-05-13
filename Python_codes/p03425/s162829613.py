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
    n = int(ipt())
    d = defaultdict(int)
    for _ in range(n):
        si = input()
        d[si[0]] += 1
    dn = {0:"M",1:"A",2:"R",3:"C",4:"H"}
    ans = 0
    for j in itertools.combinations(range(5),3):
        ans += d[dn[j[0]]]*d[dn[j[1]]]*d[dn[j[2]]]
    print(ans)
    return None

if __name__ == '__main__':
    main()
