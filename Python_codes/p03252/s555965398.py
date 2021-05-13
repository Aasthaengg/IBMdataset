#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
from collections import defaultdict
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
dic_s = defaultdict(str)
dic_t = defaultdict(str)
s = input()
t = input()
# sets = sorted(list(set(s)))
# sett

for i in range(len(s)):
    if dic_s[s[i]] or dic_t[t[i]]:
        #print(s[i],t[i],dic[s[i]], dic[t[i]])
        if dic_s[s[i]] == t[i] and dic_t[t[i]] == s[i]:
            pass
        else:
            print('No')
            exit()
    else:
        dic_s[s[i]] = t[i]
        dic_t[t[i]] = s[i]
print("Yes")
