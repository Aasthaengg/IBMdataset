import numpy as np

n, k = map(int, input().split())
A = np.array(input().split(), dtype = np.int64)
score = np.array([0 for i in range(n- k + 1)], dtype = np.int64)
wknum = 1
for i  in range(k):
    wknum *= A[i]

for i in range(n - k):
    wknum //= A[i]
    wknum *= A[k + i]
    if A[i] >= A[k + i]:
        print('No')
    else:
        print('Yes')
