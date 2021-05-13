import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@jit
def main(n, d):
  d_sort = np.sort(d)
  num = len(d_sort)//2
  return d_sort[num]-d_sort[num-1]


n = int(readline())
d = np.array(readline().split(), np.int64)


print(main(n, d))