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
    n,p = readInts()
    m = 0
    A = readInts()
    for i in range(n):
        a = A[i]
        if a % 2 == 1:
            m += 1
    if m == 0:
        print(2**n if p == 0 else 0)
    else:
        print(2**(n-1))
if __name__ == '__main__':
  main()
