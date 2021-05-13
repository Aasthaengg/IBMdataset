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
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
n = I()
B = 0
A = 0
ans = 0
BA = 0
for i in range(n):
    s = input()
    ans += s.count('AB')
    if len(s)!=1:
        if s[0] == 'B' and s[-1] == 'A':
            BA += 1
        elif s[0] == 'B':
            B += 1
        elif s[-1] == 'A':
            A += 1
print(ans + BA + min(A,B) if A!= 0 or B!=0 else ans + max(0,BA-1))
