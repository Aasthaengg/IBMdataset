
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
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7

def main():
  n = int(readline())
  if n == 0:
    print(0)
    sys.exit()
  ans = ''
  while n!=0:
    if n%2==0:
      ans = '0' + ans
      n = n//(-2)
    else:
      ans = '1' + ans
      n=(n-1)//(-2)
  print(ans)
  
  
  
  
if __name__ == '__main__':
  main()