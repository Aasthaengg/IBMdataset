import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    S = input()

    l = 0
    r = 0
    flag = False
    for i in range(len(S)):
        if not flag and S[i]=='A':
            l = i
            flag = True
        elif S[i]=='Z':
            r = i
    print(r - l + 1)


if __name__ == '__main__':
    main()
