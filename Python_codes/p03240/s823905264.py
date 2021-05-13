# import sys
# import math #sqrt,gcd,pi
# import decimal
# import queue # queue
# import bisect
# import heapq # priolity-queue
# import time
# from itertools import product,permutations,\
#     combinations,combinations_with_replacement
# 重複あり順列、順列、組み合わせ、重複あり組み合わせ
# import collections # deque
# from operator import itemgetter,mul
# from fractions import Fraction
# from functools import reduce

mod = int(1e9+7)
# mod = 998244353
INF = 1<<50

def readInt():
    return list(map(int,input().split()))

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    c = [0] * n
    for i in range(n):
        a[i],b[i],c[i] = readInt()
    for i in range(101):
        for j in range(101):
            for k in range(max(c),max(c)+105):
                res = False
                for l in range(n):
                    if max(k-abs(a[l]-i)-abs(b[l]-j),0)!=c[l]:
                        res = True
                        break
                if res:
                    continue
                else:
                    print(i,j,k)
                    return
    return

if __name__=='__main__':
    main()
