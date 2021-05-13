from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def MAP1()  : return map(lambda x:int(x)-1,input().split())
def LIST()  : return list(MAP())

def solve():
    H, W = MAP()
    a = [input() for _ in range(H)]
    d = defaultdict(int)

    for i in range(H):
        for j in range(W):
            d[a[i][j]] += 1
    
    mod4 = 0
    mod2 = 0
    for x in d.values():
        mod4 += x % 4
        mod2 += x % 2
    
    ans = "No"
    if H % 2 == 0:
        if W % 2 == 0:
            if mod4 == 0:
                ans = "Yes"
        else:
            if mod4 <= H and mod2 == 0:
                ans = "Yes"
    elif H % 2 == 1:
        if W % 2 == 0:
            if mod4 <= W and mod2 == 0:
                ans = "Yes"
        else:
            if mod4 <= W+H-1 and mod2 == 1:
                ans = "Yes"

    print(ans)

if __name__ == '__main__':
    solve()