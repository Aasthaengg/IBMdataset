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
A = readInts()
cnt = 0
i = 0
while i < n:
    # まず同じ値を処理する
    if i+1 < n:
        while A[i+1] == A[i]:
            i += 1
    # その次の者が大きい?
    if i+1 < n:
        if A[i] <= A[i+1]:
            while A[i] <= A[i+1]:
                i += 1
                if i+1 < n:
                    pass
                else:
                    break
        else:
            while A[i] >= A[i+1]:
                i += 1
                if i + 1 < n:
                    pass
                else:
                    break
    cnt += 1
    i += 1
print(cnt)
