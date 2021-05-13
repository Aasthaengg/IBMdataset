import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

H,W,A,B = map(int,read().split())

X = np.zeros((H,W),np.int8)

X[:B,:A] = 1
X[B:,A:] = 1

print('\n'.join(''.join(row) for row in X.astype(str)))