import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    ans = 0
    button = 1
    for i in range(n):
        button = A[button-1]
        ans += 1
        if button == 2:
            print(ans)
            return
    print(-1)


if __name__ == '__main__':
    main()
