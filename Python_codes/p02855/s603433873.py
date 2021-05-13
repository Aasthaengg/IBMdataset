import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np


H, W, K = map(int,readline().split())
grid = np.frombuffer(read(),'S1').reshape(H, -1)[:,:W]
X, Y = np.where(grid == b'#')
A = np.zeros((H, W),np.int32)
A[X, Y] = np.arange(1, K+1)
np.maximum.accumulate(A, axis=1, out=A)
for w in range(W-2,-1,-1):
    A[:,w] += A[:,w+1] * (A[:,w] == 0)
for h in range(1,H):
    if A[h,-1] == 0:
        A[h] += A[h-1]
for h in range(H-1,-1,-1):
    if A[h,-1] == 0:
        A[h] += A[h+1]
print('\n'.join(' '.join(row) for row in A.astype(str)))
