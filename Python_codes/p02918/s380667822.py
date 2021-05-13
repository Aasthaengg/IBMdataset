import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np

N,K = map(int,input().split())

S = np.array(list(input()), dtype='U1')

x = np.count_nonzero(S[1:] == S[:-1])

x += 2*K
x = min(x, N-1)
print(x)
