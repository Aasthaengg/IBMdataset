#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
import decimal
import re
#import bisect
#
#    d = m - k[i] - k[j]
#    if kk[bisect.bisect_right(kk,d) - 1] == d:
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
n,m = readInts()
AB = []
for i in range(n):
    a,b = readInts()
    AB.append((a,b))
AB = sorted(AB, key = lambda x:x[0])
#print(AB)
num = 0
cost = 0
for a,b in AB:
    if m >= num + b:
        num += b
        cost += a*b
    else:
        cost += a*(m - num)
        num = m
print(cost)
