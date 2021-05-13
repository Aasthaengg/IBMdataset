import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@jit
def main(n ,m ,x, a):
  ans = 0
  right = (x > a).sum()
  left = (x < a).sum()
  return min(right, left)
  
n, m, x = map(int, readline().split())
a = np.array(readline().split(), np.int64)
print(main(n, m, x, a))