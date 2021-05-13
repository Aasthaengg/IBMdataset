import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():

    a,b,c = map(int, input().split())

    if a==b:
        print(c)
    elif b==c:
        print(a)
    else:
        print(b)


if __name__ == '__main__':
    main()
