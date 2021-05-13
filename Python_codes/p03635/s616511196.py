from heapq import heappush, heappop
from itertools import permutations, accumulate
import math
import bisect
from collections import defaultdict, deque
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000000)
# MOD = 10 ** 9 + 7
# INF = float("inf")

def main():
    n, m = map(int, input().split())
    print((n-1) * (m-1))

if __name__ == "__main__":
    main()