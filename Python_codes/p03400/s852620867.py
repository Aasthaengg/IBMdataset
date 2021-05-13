import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@jit
def main(n, d, x, a):
  ans = n + x
  for i in a:
    ans += (d-1)//i
  return ans

n,d,x,*a = map(int, read().split())
print(main(n,d,x,a))