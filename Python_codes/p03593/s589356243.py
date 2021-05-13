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
h,w = readInts()
S = ""
for i in range(h):
    S += input()
LIST = Counter(S)
if h%2 == 0 and w%2 == 0:
    for k,v in LIST.items():
        if v%4:
            print('No')
            exit()
elif (h%2 == 0 and w%2) or (h%2 and w%2 == 0):
    two = 0
    for k,v in LIST.items():
        if v%2 or v%4 == 3:
            print('No')
            exit()
        if v%4 == 2:
            two += 1
    if h%2 == 0:
        if two > h//2:
            print('No')
            exit()
    else:
        if two > w//2:
            print('No')
            exit()
else:
    odd = 0
    two = 0
    for k,v in LIST.items():
        if v%4 == 1:
            odd += 1
        if v%4 == 2:
            two += 1
        if v%4 == 3:
            print('No')
            exit()
    if odd != 1:
        print('No')
        exit()
    if two > ((h-1)//2 + (w-1)//2):
        print('No')
        exit()
print('Yes')
