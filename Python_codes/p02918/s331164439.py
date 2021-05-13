from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson, minimum_spanning_tree
from scipy.sparse import csr_matrix, coo_matrix, lil_matrix
import numpy as np
from collections import deque, Counter, defaultdict
from itertools import product, permutations,combinations
from operator import itemgetter
from heapq import heappop, heappush, heapify
from bisect import bisect_left, bisect_right, bisect
from fractions import gcd
from math import ceil,floor, sqrt, cos, sin, pi, factorial
from functools import reduce
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7
def lcm_base(a, b):
    return (a * b) // gcd(a, b)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def main():
  N, M = map(int,readline().split())
  S = np.array(list(input()), dtype='U1')
  x = np.count_nonzero(S[1:] == S[:-1])
  
  x += 2*M
  x = min(x, N-1)
  print(x)
  
if __name__ == '__main__':
  main()