import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@jit
def main(n, k):
    n = n%k
    return min(n, abs(n-k))


n, k = map(int, readline().split())

print(main(n, k))