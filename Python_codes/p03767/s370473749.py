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
    n = int(input())
    A = readInts()
    # どうせ大きいやつはとられるしな
    A = sorted(A)
    #print(A)
    ans = 0
    #print(len(A)-1,len(A)-n-1)
    for i in range(len(A)-2,len(A)-2*n-1,-2):
        #print(A[i])
        ans += A[i]
    print(ans)
if __name__ == '__main__':
  main()
