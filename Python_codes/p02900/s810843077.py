#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations # (string,3) 3回
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
# def yaku(m):
#         ans = []
#         i = 1
#         while i*i <= m:
#             if m % i == 0:
#                 j = m // i
#                 ans.append(i)
#                 if j != i:
#                     ans.append(j)
#             i += 1
#         ans = sorted(ans)
#         return ans
a,b = readInts()
# print(yaku(a))
# print(yaku(b))
g = gcd(a,b)
# print(g)
# print(yaku(g))
def soinsu(n):
    dic = defaultdict(int)
    i = 2
    while i*i <= n:
        if n%i == 0:
            dic[i] += 1
            n //= i
        else:
            i += 1
    if n!= 1:
        dic[n] += 1
    return dic
dic = soinsu(g)
cnt = 1 # 1
for k,v in dic.items():
    cnt += 1
print(cnt)
# a //= g
# b //= g
# print(a,b)
