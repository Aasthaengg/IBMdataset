import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@jit
def main(s):
  ans = 0
  for j, i in enumerate(s):
    if i=='A' or i=='C' or i=='G' or i=='T':
      cnt = 1
      j += 1
      while s[j]=='A' or s[j]=='C' or s[j]=='G' or s[j]=='T':
        j += 1
        cnt += 1
      ans = max(ans, cnt)
  return ans
        
s = str(readline().split())
print(main(s))