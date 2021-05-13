#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
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
N = I()
H = readInts()
NYA = [0] * N
for i in range(N-1,-1,-1):
    if i == N-1:
        prv = H[i]
    else:
        if prv <= H[i]:
            prv = H[i]
            NYA[i] = NYA[i+1] + 1
        else:
            prv = H[i]
print(max(NYA))
