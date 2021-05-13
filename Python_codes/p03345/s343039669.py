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
    a,b,c,k = readInts()
    a_ = b + c
    b_ = a + c
    ab = a_ - b_
    k = k % 2
    if ab >= 10**18:
        print("Unfair")
    else:
        if k == 0:
            print(a-b)
        else:
            print(ab*(-1)**(k+1))

if __name__ == '__main__':
  main()
