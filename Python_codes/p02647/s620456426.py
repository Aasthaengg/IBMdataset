# 東京海上日動 プログラミングコンテスト2020 C
import numpy as np
from numba import njit
n, k = map(int, input().split())
A = np.array(list(map(int, input().split())), dtype=np.int64)

@njit
def imos(n, A):
    B = np.zeros(n+1, dtype=np.int64)
    for i in range(n):
        left = max(0, i - A[i])
        right = min(n, i + A[i] + 1)
        B[left] += 1
        B[right] -= 1
    B = np.cumsum(B)
    return B[:-1]

def solve(n,k,A):
    for i in range(k):
        A = imos(n, A)
        min_A = min(A)
        if min_A == n:
            return A
    return A

ANS = solve(n, k, A)
print(' '.join(map(str, ANS)))