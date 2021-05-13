import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    n,m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]
    CD = [list(map(int, input().split())) for _ in range(m)]

    for i in range(n):
        dist = []
        for j in range(m):
            dist.append(abs(AB[i][0]-CD[j][0]) + abs(AB[i][1] - CD[j][1]))
        dist_min = min(dist)
        for k in range(len(dist)):
            if dist[k] == dist_min:
                print(k+1)
                break


if __name__ == '__main__':
    main()
