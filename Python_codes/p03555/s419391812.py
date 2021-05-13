import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    C = input()
    C2 = input()

    for i in range(3):
        if C[i] != C2[2-i]:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    main()
