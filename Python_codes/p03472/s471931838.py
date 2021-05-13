#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
#from collections import defaultdict
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
n,h = readInts()
a = [0] * n
b = [0] * n
for i in range(n):
    a_,b_ = readInts()
    a[i] = a_;b[i]=b_;
a = sorted(a,reverse = True)
b = sorted(b,reverse = True)
MAX = a[0]
ans = 0
for v in b:
    if h <= 0:
        break
    if v > MAX:
        ans += 1
        h -= v
    else:
        break
if h > 0:
    ans += (h+MAX-1)//MAX
print(ans)
