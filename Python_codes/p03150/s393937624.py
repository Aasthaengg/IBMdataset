#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
from collections import defaultdict
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
s = list(input())
nya = list("keyence")
slen = len(s)
for i in range(slen):
    #rint(s[:i],nya[:i],s[-7+i:],nya[-7+i:])
    if s[:i] == nya[:i] and s[-7 + i:] == nya[-7 + i:]:
        print('YES')
        exit()
print('NO')
