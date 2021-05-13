import numpy as np
N = int(input())
A = np.array(list(map(int, input().split()))) - np.array(list(range(1, N+1)))
A = A.astype(np.int64)
m = np.median(A)
m = m.astype(np.int64)
A -= m
ans = sum(np.abs(A))
print(ans.astype(np.int64))