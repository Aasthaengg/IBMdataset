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
def LIST1() : return list(MAP1())

def solve():
    N, M = MAP()
    d = defaultdict(int)
    for i in range(M):
        a, b = MAP()
        d[a] += 1
        d[b] += 1

    ans = "YES"
    for x in d.values():
        if x % 2 == 1:
            ans = "NO"
    print(ans)

if __name__ == '__main__':
    solve()