# from fractions import gcd
# from datetime import date, timedelta
# from heapq import*
# import math
from collections import defaultdict, Counter, deque
# import sys
# from bisect import *
# import itertools
# import copy
# sys.setrecursionlimit(10 ** 7)
# MOD = 10 ** 9 + 7


def main():
    n = int(input())
    print(0)
    v = input()
    if v == "Vacant":
        exit()
    l, r = 0, n - 1
    while True:
        m = (l+r)//2
        print(m)
        q = input()
        if q == "Vacant":
            exit()
        elif m % 2 != 0:
            if v == q:
                r = m 
            else:
                l = m + 1
        else:
            if v == q:
                l = m+1
            else:
                r = m 


if __name__ == '__main__':
    main()
