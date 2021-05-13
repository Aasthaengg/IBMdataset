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
# my_round_int = lambda x:np.round((x*2 + 1)//2)
# 四捨五入g
import sys
sys.setrecursionlimit(10000000)
#mod = 10**9 + 7
#mod = 9982443453
mod = 998244353
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
k,n = readInts()
A = readInts()
max_dist = 0
for i in range(n):
    next = (i+1)%n
    dist = A[next] - A[i]
    if dist < 0:
        dist += k
    max_dist = max(max_dist, dist)
print(k - max_dist)
