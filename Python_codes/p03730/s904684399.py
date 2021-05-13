import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    a,b,c = map(int, input().split())

    for i in range(100):
        if (a*(i+1))%b == c:
            print('YES')
            return
    print('NO')


if __name__ == '__main__':
    main()
