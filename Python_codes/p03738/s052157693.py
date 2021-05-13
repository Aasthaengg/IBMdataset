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
    a = int(input())
    b = int(input())
    if a>b:
        print("GREATER")
    elif a<b:
        print("LESS")
    else:
        print("EQUAL")
    return

if __name__=='__main__':
    main()
