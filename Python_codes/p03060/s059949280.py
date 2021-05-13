#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from itertools import combinations # (string,3) 3回
#from collections import deque
#import collections.defaultdict(list)
#import bisect
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    n = int(input())
    V = readInts()
    C = readInts()
    ans = -1
    for bit in range(1 << n):
        # bit 全探索
        cost = 0
        value = 0
        for i in range(n):
            if bit & (1 << i):
                # もしフラグが立っていたら、
                cost += C[i]
                value += V[i]
        ans = max(ans,value - cost)
    print(ans)
if __name__ == '__main__':
  main()
