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
#mod = 10**9 + 7
mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
n = int(input())
s = input()
t = input()
cnt = 0
ans = 0
for i in range(len(s)):
    if s[i] == t[cnt]:
        cnt += 1
    elif s[i] != t[cnt] and s[i] == t[0]:
        ans = max(ans,cnt)
        cnt = 1
    else:
        ans = max(ans,cnt)
        cnt = 0
print(n + n - cnt)
