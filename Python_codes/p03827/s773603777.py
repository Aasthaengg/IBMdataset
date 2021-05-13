import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    n = int(input())
    S = input()

    array = [0]
    for i in range(len(S)):
        if S[i] == 'I':
            array.append(array[i]+1)
        if S[i] == 'D':
            array.append(array[i]-1)
    print(max(array))


if __name__ == '__main__':
    main()
