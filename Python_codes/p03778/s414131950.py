# import sys
# import math
# import decimal
# import queue
# import bisect
# import heapq
# import time
# import itertools
# import collections # queue
# from fractions import Fraction

mod = int(1e9+7)
INF = 1<<29
lINF = 1<<35

def main():
    w,a,b = map(int,input().split())
    ans = 0
    if a<b:
        ans = b - (a + w)
    else:
        ans = a - (b + w)
    print(max(0,ans))
    return

if __name__=='__main__':
    main()
