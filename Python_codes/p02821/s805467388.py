import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
A = np.array(lr())
A.sort()

def shake_cnt(x):
    Y = np.searchsorted(A, x-A)
    return N*N - Y.sum()

right = 10 ** 6
left = 0
while right > left + 1:
    mid = (right+left) // 2
    if shake_cnt(mid) >= M:
        left = mid
    else:
        right = mid

Acum = np.zeros(N+1, np.int64)
Acum[1:] = A.cumsum()
Y = np.searchsorted(A, right-A)
happy = (Acum[-1]-Acum[Y]).sum() + (A * (N-Y)).sum()
happy += left * (M-shake_cnt(right))
print(happy)
# 32