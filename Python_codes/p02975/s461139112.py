#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate, product # (string,3) 3回
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
n = I()
li = list(map(int,input().split()))
se = set(li)
if len(se) == 1:
    if sum(se) == 0:
        print('Yes')
    else:
        print('No')
elif len(se) == 2:
    a,b = sorted(se)
    if a == 0:
        if li.count(a) * 3 == n:
            print('Yes') # 0 count is equal 1
        else:
            print('No')
    else:
        print('No')
elif len(se) == 3:
    a,b,c = se
    if li.count(a) == li.count(b) == li.count(c):
        if a^b == c:
            print('Yes')
        else:
            print('No') # a xor b xor c = 0 is ok
    else:
        print('No')
else:
    print('No')
