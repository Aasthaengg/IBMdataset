#import numpy as np
#from numpy import*
#from scipy.sparse.csgraph import shortest_path #shortest_path(csgraph=graph) # dijkstra# floyd_warshall
#from scipy.sparse import csr_matrix

from collections import* #defaultdict Counter deque appendleft
from fractions import gcd
from functools import* #reduce
from itertools import* #permutations("AB",repeat=2) combinations("AB",2) product("AB",2) groupby accumulate
from operator import mul,itemgetter
from bisect import* #bisect_left bisect_right
from heapq import* #heapify heappop heappushpop
from math import factorial,pi
from copy import deepcopy
import sys
sys.setrecursionlimit(10**8)
#input=sys.stdin.readline  #危険！基本オフにしろ！
def cmb(n, r):
    if n-r<0:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)

def main():
    n,W=map(int,input().split())
    d=defaultdict(int)
    d[0]=0
    for i in range(n):
        w,v=map(int,input().split())
        for k,j in d.copy().items():
            if k+w<=W:
                d[k+w]=max(d[k+w],j+v)
#    print(d)
    print(max(d.values()))
if __name__ == '__main__':
    main()