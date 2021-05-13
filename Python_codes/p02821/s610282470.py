import sys
input = sys.stdin.readline
import numpy as np
N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A = np.sort(np.array(A))
def shake_hands(x):
    cnt = 0
    X = np.searchsorted(A, x - A, side="left")
    cnt += N * N - X.sum()
    if cnt >= M:
        return 1
    return 0
left = 0
right = 10 ** 6
while True:
    m = (right + left) // 2
    if shake_hands(m) == 1 and shake_hands(m+1) == 0:
        maximum = m
        break
    elif shake_hands(m) == 0 and shake_hands(m-1) == 1:
        maximum = m - 1
        break
    elif shake_hands(m) == 1:
        left = m + 1
    else:
        right = m - 1
X = np.searchsorted(A,maximum+1-A) # 行わない人数
Acum = np.zeros(N+1,np.int64) # 人数 -> 累積和
Acum[1:] = np.cumsum(A)

shake = N * N - X.sum()
happy = (Acum[-1] - Acum[X]).sum() + (A * (N - X)).sum()

happy += (M - shake) * (maximum)
print(happy)
