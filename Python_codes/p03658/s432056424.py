# import sys
# import math
# import decimal
# import queue
# import bisect
# import heapq # priolity-queue
# import time
# import itertools
# import collections # queue
# from operator import itemgetter
# from fractions import Fraction

mod = int(1e9+7)
INF = 1<<29
lINF = 1<<35

def main():
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort(reverse=True)
    ans = 0
    for i in range(k):
        ans += l[i]
    print(ans)
    return

if __name__=='__main__':
    main()
