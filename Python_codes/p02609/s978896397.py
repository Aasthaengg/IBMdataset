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
    N = INT()
    xbin = input()
    xdec = int(xbin, 2)
    m = xbin.count('1')

    a = xdec % (m+1)
    b = xdec % (m-1) if m > 1 else 0

    num = [0]*N
    for i in range(1, N):
        num[i] = num[i % bin(i).count('1')] + 1

    for i in range(N):
        if xbin[i] == '0':
            y = ( a + pow(2, N-i-1, m+1) ) % ( m+1 )
            print(num[y] + 1)
        elif m <= 1:
            print(0)
        else:
            y = ( b - pow(2, N-i-1, m-1) ) % ( m-1 )
            print(num[y] + 1)

if __name__ == '__main__':
    solve()