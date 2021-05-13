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
d,g = readInts()
P = []
C = []
res = float('inf')
for i in range(d):
    p,c = readInts()
    P.append(p)
    C.append(c)
for bit in range(1 << d):
    SUM = 0
    NUM = 0
    for i in range(d):
        if bit & (1 << i):
            SUM += 100 * (i + 1) * P[i] + C[i]
            NUM += P[i]
    if SUM >= g:
        res = min(res,NUM)
    else:
        for i in range(d-1,-1,-1):
            if bit & (1 << i):
                continue
            else:
                for j in range(P[i]):
                    if SUM >= g:
                        break
                    SUM += 100 * (i+1)
                    NUM += 1
        res = min(res,NUM)
print(res)
