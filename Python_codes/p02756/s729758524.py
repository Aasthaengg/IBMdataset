#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
import decimal
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
s = input()
q = I()
rev = False
ans = deque((s))
for i in range(q):
    A = input().split()
    if A[0] == '1':
        if rev:
            rev = False
        else:
            rev = True
    else:
        if A[1] == '1':
            if rev:
                ans.append(A[2])
            else:
                ans.appendleft(A[2])
        else:
            if rev:
                ans.appendleft(A[2])
            else:
                ans.append(A[2])
if rev:
    ans.reverse()
    print(*ans,sep='')
else:
    print(*ans,sep='')
