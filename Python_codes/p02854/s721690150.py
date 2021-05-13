#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
#from collections import deque,defaultdict
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
# n = I()
# A = readInts()
# div = sum(A)//2
# nya = 0
# pivot = 0
# for i in range(n):
#     nya += A[i]
#     if nya >= div:
#         pivot = i
#         break
# #print(i)
# print(abs(sum(A[i+1:]) - nya))
n = int(input())
A = readInts()
# 全体の合計
total = sum(A)
mi_ = float('inf')
left = 0
for i in range(n):
    left += A[i]
    total -= A[i]
    mi_ = min(mi_, abs(left - total))
print(mi_)
