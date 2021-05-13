import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A = np.array(read().split(), np.int64)[1:]

A.sort()
Acum = A.cumsum()

ng = Acum[:-1] * 2 < A[1:]
ng = np.logical_or.accumulate(ng[::-1])[::-1]
x = (~ng).sum() + 1
print(x)