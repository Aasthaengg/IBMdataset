import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, readline().split())
A = np.array(read().split(), np.int32)

g = np.gcd.reduce(A)
cond = (K % g == 0) and (K <= A.max())
print('POSSIBLE' if cond else 'IMPOSSIBLE')