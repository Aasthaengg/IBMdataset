#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate, product # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
import decimal
import re
import math
import bisect
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#
# my_round_int = lambda x:np.round((x*2 + 1)//2)
# 四捨五入g
#
# インデックス系
# int min_y = max(0, i - 2), max_y = min(h - 1, i + 2);
# int min_x = max(0, j - 2), max_x = min(w - 1, j + 2);
#
#
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
#mod = 998244353
from sys import stdin
readline = stdin.readline
def readInts():
  return list(map(int,readline().split()))
def readTuples():
    return tuple(map(int,readline().split()))
def I():
  return int(readline())
s = input()
ln = len(s)
if ln%2 == 0:
    ml = ln//2 - 1
    mr = ln//2
    ans = 0
    for i in range(ml+1):
        #print(s[i],s[-i-1])
        if s[i] == s[-i-1]:
            pass
        else:
            ans += 1
else:
    m = ln//2
    ans = 0
    for i in range(m):
        if s[i] == s[-i-1]:
            pass
        else:
            ans += 1
print(ans)
