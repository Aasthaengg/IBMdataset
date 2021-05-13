import numpy as np
N = int(input())
A = np.array(input().split(), dtype=int)
A.sort()

B = np.cumsum(A)

ans = 0
for i in range(N - 1):
    if B[i] * 2 >= A[i + 1]:
        ans += 1
    else:
        ans = 0

ans += 1
print(ans)
