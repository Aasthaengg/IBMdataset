import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@jit
def main(n):
  ans = [n]
  m = 0
  while not ans[m] in ans[:m]:
    if n%2 == 0:
      n /= 2
      ans.append(n)
    else:
      n = 3 * n + 1
      ans.append(n)
    m += 1
  return m+1
    
    
  
n = int(input())
print(main(n))