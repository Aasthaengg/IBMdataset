import sys
import itertools
sys.setrecursionlimit(10000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy

if __name__ == "__main__":
    n = int(input())
    print(int(n**0.5)**2)