import numpy as np

N, K, Q = map(int, input().split())
A = np.zeros(N, dtype=int)

for i in range(Q):
    A[int(input()) - 1] += 1

for ai in A:
    print(['No', 'Yes'][int(ai) + K - Q > 0])