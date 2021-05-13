import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    h,w = map(int, input().split())
    A = [input() for _ in range(h)]

    print('#'*(w+2))
    for i in range(h):
        print('#' + A[i] + '#')
    print('#'*(w+2))


if __name__ == '__main__':
    main()
