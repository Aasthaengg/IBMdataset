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
    n = int(input())
    LIST = [0] * 100001
    for i in range(n):
        l,r = readInts()
        l -=1
        # いもす法
        LIST[l] +=1
        LIST[r] -=1
    # 累積和
    for i in range(1,100001):
        LIST[i] += LIST[i-1]
    cnt = 0
    for i in range(100001):
        if LIST[i] > 0:
            cnt += 1
    #print(LIST)
    print(cnt)
if __name__ == '__main__':
  main()
