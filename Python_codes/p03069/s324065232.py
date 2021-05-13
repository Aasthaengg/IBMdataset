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
n = I()
S = list(input())
white = [0] * (n+1)
black = [0] * (n+1)
for i in range(n):
    white[i+1] = white[i]  + (1 if S[i] == '.' else 0)
    black[i+1] = black[i] + (1 if S[i] == '#' else 0)
res = float('inf')
# 累積和で最小値を求める
for left in range(n+1):
    tmp = 0
    # leftを全部白に、
    tmp += black[left] - black[0]
    tmp += white[n] - white[left]
    res = min(res,tmp)
print(res)
