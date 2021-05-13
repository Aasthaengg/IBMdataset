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
def main():
    n = int(input())
    vx = []
    vy = []
    vh = []
    for i in range(n):
        x,y,h = readInts()
        vx.append(x)
        vy.append(y)
        vh.append(h)
        if h > 0:
            si = i
    # 基準となる座標はどこでもいい
    # けど、h = 0 のところはだめやねん
    #
    resx,resy,resh = -1,-1,-1
    for x in range(101):
        for y in range(101):
            h = vh[si] + abs(x - vx[si]) + abs(y - vy[si])
            ok = True
            for i in range(n):
                if vh[i] > 0 and h - vh[i] != abs(x - vx[i]) + abs(y - vy[i]):
                    ok = False
                if vh[i] == 0 and h > abs(x - vx[i]) + abs(y - vy[i]):
                    ok = False
            if ok:
                resx = x
                resy = y
                resh = h
    print(resx,resy,resh)
if __name__ == '__main__':
  main()
