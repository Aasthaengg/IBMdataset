import numpy as np
n = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
C = np.array([a-b for a, b in zip(A, B)], dtype='int64')
C.sort()
cnt_neg = np.sum(C < 0)
cnt_pos = np.sum(C > 0)
sum_neg = -1 * np.sum(C[C < 0])
sum_pos = np.sum(C[C > 0])
if sum_pos - sum_neg < 0:
    print(-1)
elif sum_neg == 0:
    print(0)
else:
    C = C[C>0]
    C.sort()
    C = C[::-1]
    C = np.cumsum(C)
    print(cnt_neg + np.count_nonzero(C < sum_neg) + 1)