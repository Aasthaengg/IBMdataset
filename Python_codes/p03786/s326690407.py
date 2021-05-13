import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))
A.sort()
B = np.cumsum(A)

cnt = 1
for i in range(N-1):
    if B[i]*2 >= A[i+1]:
        cnt += 1
    else:
        cnt = 1

print(cnt)
