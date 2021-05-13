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
    n,m = readInts()
    s = input()
    t = input()
    from fractions import gcd
    g = gcd(n,m)
    res = n // g * m
    # 互いに素なn,mを作成する
    n //= g
    m //= g
    ok = True
    for i in range(g):
        # 0 ~ (g-1)まで調べる
        if s[i*n] != t[i*m]:
            ok = False
    if ok:
        print(res)
    else:
        print(-1)
if __name__ == '__main__':
  main()
