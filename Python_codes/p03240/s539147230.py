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
x = [];y=[];h=[]
sh = -1
for i in range(n):
    xa,ya,ha = readInts()
    x.append(xa);y.append(ya);h.append(ha);
    if ha > 0:
        sh = i
# CxとCyを特定しておく すべてにおいて合致するかを考える
resx = -1;resy =-1;resh=-1;
for Cx in range(101):
    for Cy in range(101):
        ok = True
        H = h[sh] + abs(x[sh] - Cx) + abs(y[sh] - Cy)
        # 全操作して合致するようにする
        for i in range(n):
            if h[i] == 0:
                if H > abs(x[i] - Cx) + abs(y[i] - Cy):
                    ok = False
                    break
            elif h[i] > 0:
                if H -h[i] !=  abs(x[i] - Cx) + abs(y[i] - Cy):
                    ok = False
                    break
        if ok:
            resx = Cx;resy = Cy;resh = H;

print(resx,resy,resh)
