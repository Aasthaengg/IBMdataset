import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    x,y = map(int, input().split())

    ans = 0
    while x <= y:
        x *= 2
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
