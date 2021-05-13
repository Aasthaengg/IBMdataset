import sys
# import math
# import decimal
# import queue
# import bisect
# import heapq
# import time
# import itertools
# from fractions import Fraction

mod = int(1e9+7)
INF = 1<<29

def main():
    n,k = map(int,input().split())
    if n==1:
        print(k)
        return
    ans = k * ((k - 1) ** (n - 1))
    print(ans)
    return

if __name__=='__main__':
    main()
