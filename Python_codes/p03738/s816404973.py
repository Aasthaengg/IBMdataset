import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    a = int(input())
    b = int(input())

    if b < a:
        print('GREATER')
    elif a == b:
        print('EQUAL')
    else:
        print('LESS')


if __name__ == '__main__':
    main()
