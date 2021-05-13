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
# my_round_int = lambda x:np.round((x*2 + 1)//2)
# 四捨五入
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
n,m = readInts()
A = [list(input()) for _ in range(n)]
B = [list(input()) for _ in range(m)]
def search(j,i):
    for k in range(m):
        for s in range(m):
            if A[j+k][i+s] != B[k][s]:
                return False
            else:
                continue
    return True
flag = False
for i in range(n-m+1):
    for j in range(n-m+1):
        if A[j][i] == B[0][0]:
            if search(j,i):
                print('Yes')
                exit()
print('No')
