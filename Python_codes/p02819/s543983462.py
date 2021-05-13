import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = int(input())

@jit
def main(s):
  while True:
    flag = False
    for i in range(2, int(s**(1/2)+1)):
      if s%i == 0:
        flag = True
    if not flag:
      return s
    s += 1
print(main(s))