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
    n, m = readInts()
    # mが成功する確率は(1/2)^mであるから、期待値は
    # ACするまでに施行する回数の期待値は、2^m
    # 普通のプログラムは、
    # 1900M + 100(N - M)ms かかることから、
    # 2^m * (1900M + 100(N-M))
    AC = (1 << m) # 2^m
    Expect = 1900 * m + 100 * (n-m)
    print(AC * Expect)
if __name__ == '__main__':
  main()
