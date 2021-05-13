import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    a,b,c,d = map(int, input().split())

    l = a + b
    r = c + d
    if l > r:
        print('Left')
    elif l < r:
        print('Right')
    else:
        print('Balanced')


if __name__ == '__main__':
    main()
