from math import ceil,floor,comb,factorial,gcd,pow,sqrt,log2,cos,sin,tan,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heappop,heappush
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
v = LIST()

e = Counter(v[0:n:2])
o = Counter(v[1:n:2])

if e.most_common()[0][0] != o.most_common()[0][0]:
    ans = n - e.most_common()[0][1] - o.most_common()[0][1]
else:
    try:
        tmp0 = n - e.most_common()[0][1] - o.most_common()[1][1]
    except:
        tmp0 = n - e.most_common()[0][1]
    try:
        tmp1 = n - e.most_common()[1][1] - o.most_common()[0][1]
    except:
        tmp1 = n - o.most_common()[0][1]
    ans = min( tmp0, tmp1 )

print( ans )