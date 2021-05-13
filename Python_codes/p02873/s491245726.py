#from statistics import median
import collections
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

S = input()
ln = len(S)
ans = [0] * (ln+1)
# 前から
for i in range(ln):
    if S[i] == '<':
        ans[i+1] = max(ans[i+1],ans[i]+1)
#print(ans)
# 後ろから
for i in range(ln-1,-1,-1):
    if S[i] == '>':
        ans[i] = max(ans[i],ans[i+1]+1)
#print(ans)
print(sum(ans))
