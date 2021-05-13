import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    S = input()

    if len(S) == len(set(S)):
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
