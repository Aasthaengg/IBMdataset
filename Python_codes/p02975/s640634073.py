from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
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
def LIST()  : return list(MAP())

n = INT()
a = LIST()
c = Counter(a).most_common()

if len(c) == 3 and c[0][1] == c[1][1] == c[2][1]:
    x = c[0][0]
    y = c[1][0]
    z = c[2][0]
    if x^y^z == 0:
        ans = "Yes"
    else:
        ans = "No"
elif len(c) == 2 and c[0][1] == 2*c[1][1]:
    x = c[0][0]
    y = c[1][0]
    if x^x^y == 0:
        ans = "Yes"
    else:
        ans = "No"
elif len(c) == 1 and c[0][0] == 0:
    ans = "Yes"
else:
    ans = "No"

print(ans)