from math import ceil,floor,comb,factorial,gcd,pow,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

sx, sy, tx, ty = MAP()
dx = tx - sx
dy = ty - sy

print('U'*dy+'R'*dx+'D'*dy+'L'*dx+'L'+'U'*(dy+1)+'R'*(dx+1)+'D'+'R'+'D'*(dy+1)+'L'*(dx+1)+'U')