from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations # (string,3) 3回
from collections import deque
from collections import defaultdict
import bisect
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

def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
n = I()
A,B = readInts()
P = sorted(readInts())
i = 0
nya = 0
ans = 0
while i < n:
    if nya == 0:
        if 1 <= P[i] <= A:
            nya = 1
            P[i] = -1
    elif nya == 1:
        if A < P[i] <= B:
            nya = 2
            P[i] = -1
    elif nya == 2:
        if B < P[i]:
            nya = 0
            P[i] = -1
            ans += 1
            i = 0
    i += 1
#print(P)
print(ans)
