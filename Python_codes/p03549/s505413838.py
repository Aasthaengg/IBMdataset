# import sys
# import math #sqrt,gcd
# import decimal
# import queue # queue
# import bisect
# import heapq # priolity-queue
# import time
from itertools import product,permutations,combinations,combinations_with_replacement
# 重複あり順列、順列、組み合わせ、重複あり組み合わせ
# import collections # deque
# from operator import itemgetter,mul
# from fractions import Fraction
# from functools import reduce

mod = int(1e9+7)
INF = 1<<29
lINF = 1<<35

def readInt():
    return list(map(int,input().split()))

def main():
    n,m = readInt()
    ans = (n - m) * 100 + 1900 * m
    TLE = 2 ** m
    print(ans*TLE)
    return

if __name__=='__main__':
    main()