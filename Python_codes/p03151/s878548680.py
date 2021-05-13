#from statistics import median
import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
#from collections import deque,defaultdict
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
n = I()
A = readInts()
B = readInts()
num = 0
minus = 0
box = []
for i in range(n):
    diff = A[i] - B[i]
    if diff < 0:
        minus -= diff
        num += 1
    else:# プラスの分を足していく
        box.append(diff)
box = sorted(box,reverse = True)
if num == 0:
    print(0)
else:
    # 大きい方から＋の和を取っていって、それが－の合計以上になったらもうやらなくていいよ
    plus = 0
    for a in box:
        plus += a
        num += 1
        if plus >= minus:
            break
    if plus >= minus:
        print(num)
    else:
        print(-1)
