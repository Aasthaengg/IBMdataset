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
W,H,N = readInts()
field = [[False] * W for _ in range(H)]

def fill(sy,sx,gy,gx):
    cnt = 0
    for y in range(sy,gy):
        for x in range(sx,gx):
            if field[y][x]:
                continue
            else:
                field[y][x] = True
                #print(y,x)
                cnt += 1
    return cnt
ans = 0
for i in range(N):
    x,y,a = readInts()
    if a == 1:
        ans += fill(0,0,H,x)
    elif a == 2:
        ans += fill(0,x,H,W)
    elif a == 3:
        ans += fill(0,0,y,W)
    else:
        ans += fill(y,0,H,W)
    #print(ans)
print(H*W - ans)
