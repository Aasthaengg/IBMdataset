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
    n,a,b,*v=map(int,open(0).read().split())
    v.sort(reverse=1)
    m=sum(v[:a])/a
    print(m)
    n=v[a-1]
    x,y=v[:a].count(n),v.count(n)
#    print(x,y)
    ans=0
    if m==n and y-x>0:
        for i in range(x,x+b-a+1):
            ans+=cmb(y,i)
        print(ans)
    else:
        print(cmb(y,x))

if __name__ == '__main__':
    main()
