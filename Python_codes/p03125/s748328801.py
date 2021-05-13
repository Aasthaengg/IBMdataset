import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

A, B = [int(x) for x in readline().rstrip().split()]
if B % A == 0:
    print(A + B)
else:
    print(B - A)
