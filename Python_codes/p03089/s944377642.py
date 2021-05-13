#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict
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
b = readInts()
ans = []
for i in range(n):
    pivot = -1
    for j in range(len(b)-1,-1,-1):
        if b[j] == j+1:
            pivot = j
            break
    if pivot == -1:
        print(-1)
        exit()
    ans.append(pivot+1)
    b.pop(pivot)
print(*ans[::-1],sep='\n')
