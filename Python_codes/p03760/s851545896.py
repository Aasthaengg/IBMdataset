import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections

def main():
    O = input()
    E = input()

    ans = ''
    for i in range(len(O)):
        ans += O[i]
        if i < len(E):
            ans += E[i]
    print(ans)


if __name__ == '__main__':
    main()
