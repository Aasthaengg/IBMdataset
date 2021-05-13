import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from heapq import heappop,heappush,heapify

@jit
def main(n, a):
  for _ in range(1, n):
    x = heappop(a)
    y = heappop(a)
    heappush(a, (x + y)/2)
  return a[0]

n,*a = map(int,read().split())
heapify(a)
print(main(n,a))