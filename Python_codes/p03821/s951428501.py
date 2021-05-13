import numpy as np

N = int(input())
A = np.zeros(N).astype(int)
B = np.zeros(N).astype(int)

for i in range(N):
    A[i], B[i] = map(int, input().split())

ans = 0
for i in reversed(range(N)):
    A[i] = A[i] + ans
    if A[i] % B[i] == 0:
        continue
    elif B[i] - A[i] > 0:
        ans += B[i] - A[i]
    else:
        ans += B[i] - (A[i] % B[i])
    
print(ans)