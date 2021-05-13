#input
N, M = map(int, input().split())
A = list(map(int, input().split()))

#output
import numpy as np
A = np.array(A)
A.sort()

def number_of_shake(K):
    p = np.searchsorted(A, K-A)
    return N*N - p.sum()

left = 0
right = 10**6
while left + 1 < right:
    mid = (left + right) // 2
    if number_of_shake(mid) >= M:
        left = mid
    else:
        right = mid

L = np.searchsorted(A, right-A)
Acum = np.zeros(N+1, np.int64)
Acum[1:] = np.cumsum(A)

shake = N*N - L.sum()
happy = (Acum[-1] - Acum[L]).sum() + (A*(N-L)).sum()
happy += (M-shake)*left

print(happy)
