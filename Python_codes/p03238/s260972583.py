#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from itertools import combinations # (string,3) 3回
#from collections import deque
#import collections.defaultdict
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
sys.setrecursionlimit(10000)
mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    if input() == '1':
        print('Hello World')
    else:
        a = int(input())
        b = int(input())
        print(a+b)
if __name__ == '__main__':
  main()