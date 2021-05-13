# import sys
# import math #sqrt,gcd,pi
# import decimal
# import queue # queue
import bisect
# import heapq # priolity-queue
# from time import time
# from itertools import product,permutations,\
    # combinations,combinations_with_replacement
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
    h = readInt()
    dp = [INF for i in range(n+1)]
    dp[1] = 0
    for i in range(1,n+1):
        for j in range(i+1,i+3):
            if j>n:
                continue
            dp[j] = min(dp[j],dp[i] + abs((h[j-1]-h[i-1])))
    print(dp[n])
    return

if __name__=='__main__':
    main()
