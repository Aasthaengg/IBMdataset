from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations # (string,3) 3回
from collections import deque
from collections import defaultdict
import bisect
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

def readInts():
  return list(map(int,input().split()))
def main():
    n = input()
    if len(n) == 1:
        print(n)
        exit()
    allnine = True
    for i in range(1,len(n)):
        if n[i] == '9':
            pass
        else:
            allnine = False
    if n[0] == '9' and allnine:
        print(9 * len(n))
        exit()
    if n[0] == '1' and allnine:
        print(1 + (len(n)-1) * 9)
        exit()
    if n[0] != '1' and allnine:
        print(int(n[0]) + (len(n)-1) * 9)
        exit()
    print(int(n[0]) + (len(n)-1) * 9 - 1)

if __name__ == '__main__':
  main()
