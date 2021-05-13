#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from itertools import combinations # (string,3) 3回
#from collections import deque
#import collections.defaultdict(list)
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

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    s = input()
    for i in range(0,len(s),2):
        #print(s[i:i+2])
        if s[i:i+2] == 'hi':
            pass
        else:
            print('No')
            exit()
    print('Yes')
if __name__ == '__main__':
  main()
