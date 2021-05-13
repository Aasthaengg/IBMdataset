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
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i]=="+":
            ans += 1
        else:
            ans -= 1
    print(ans)
    return

if __name__=='__main__':
    main()
