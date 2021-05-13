# import sys
# import math #sqrt
# import decimal
# import queue # queue
# import bisect
# import heapq # priolity-queue
# import time
# from itertools import permutations #順列生成
# import collections # deque
# from operator import itemgetter
# from fractions import Fraction

mod = int(1e9+7)
INF = 1<<29
lINF = 1<<35

def readInt():
    return list(map(int,input().split()))

def main():
    n = int(input())
    k = int(input())
    ans = 1
    for i in range(n):
        ans = min(ans*2,ans+k)
    print(ans)
    return

if __name__=='__main__':
    main()