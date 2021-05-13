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
    A = []
    B = []

    for i in range(n):
        a,b = readInts()
        A.append(a)
        B.append(b)
    l = 0
    for i in range(n-1,-1,-1):
        # 前回分からだんだん加算されていくパターン
        A[i] += l
        if A[i] % B[i] == 0:
            continue
        #print("before",A[i],B[i])
        ama = A[i] % B[i] # 9 4 ≡ 1 増やす数は、4 - 1 = 3
        up_ = B[i] - ama
        #print("after",A[i]+up_,B[i])
        l += up_
    print(l)
if __name__ == '__main__':
  main()
