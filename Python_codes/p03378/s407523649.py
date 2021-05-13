import numpy as np

N, M, X = map(int, input().split())
A = np.array(list(map(int, input().split())))

ans = 0
if N <= X:
    ans = np.intersect1d(A[A > N], A[A < X]).shape[0]
else:
    ans = min(
        np.intersect1d(A[A > 0], A[A < X]).shape[0],
        np.intersect1d(A[A < N], A[A > X]).shape[0],
    )

print(ans)