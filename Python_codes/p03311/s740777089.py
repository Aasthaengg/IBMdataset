from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
#from collections import deque,defaultdict
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
n = I()
A = readInts()
for i in range(1,n+1):
    A[i-1] -= i
#print(A)
medi = median(A)
medi = int(medi) if medi - int(medi) < 0.5 else int(medi) + 1
ans = 0
for i in range(n):
    ans += abs(A[i] - medi)
print(ans)
