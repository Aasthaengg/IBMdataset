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

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    n = int(input())
    dic = {}
    for i in range(2,n+1):
        a = i
        p = 2
        while p * p <= a:
            if a % p == 0:
                if p in dic:
                    dic[p] += 1
                else:
                    dic[p] = 1
                a //=p
            else:
                p += 1
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    ans = 1
    #print(dic)
    for k,v in dic.items():
        ans *= (v+1)
    print(ans%mod)
if __name__ == '__main__':
  main()
