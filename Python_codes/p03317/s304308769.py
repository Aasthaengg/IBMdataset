
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson, minimum_spanning_tree
from scipy.sparse import csr_matrix, coo_matrix, lil_matrix
import numpy as np
from functools import reduce

from collections import deque, Counter, defaultdict
from itertools import product, permutations,combinations
from operator import itemgetter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right, bisect
from fractions import gcd
from math import ceil,floor, sqrt, cos, sin, pi, factorial
import statistics
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7
def lcm(a, b):
  return a*b//gcd(a, b)

def main():
  N, K = map(int, readline().split())
  A = list(map(int, readline().split()))
  print(ceil((N-1)/(K-1)))
  
  
  
  
  
if __name__ == '__main__':
  main()