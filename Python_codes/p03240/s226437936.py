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
n = I()
X = [];Y = [];H = []
for i in range(n):
    x,y,h = readInts()
    X.append(x)
    Y.append(y)
    H.append(h)
    if h > 0:
        si = i
resx=-1;resy=-1;resh=-1;
for cx in range(101):
    for cy in range(101):
        judge = True
        h = H[si] + abs(X[si] - cx) + abs(Y[si] - cy)
        for i in range(n):
            if H[i] == 0:
                if h > abs(X[i] - cx) + abs(Y[i] - cy):
                    judge ^=True
                    break
            else:
                if h - H[i] != abs(X[i]-cx) + abs(Y[i]-cy):
                    judge ^= True
                    break
        if judge:
            resx =cx;resy=cy;resh=h;
print(resx,resy,resh)
