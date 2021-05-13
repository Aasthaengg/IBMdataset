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
    a,b,c,d = map(int,ipt().split())
    ans = b-a+1
    ans -= b//c-(a-1)//c
    ans -= b//d-(a-1)//d
    g = c*d//math.gcd(c,d)
    ans += b//g-(a-1)//g
    print(ans)
    return

if __name__ == '__main__':
    main()
