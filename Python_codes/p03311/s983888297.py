import numpy as np
N = int(input())
A = list(map(int,input().split()))
A = [A[i] - i - 1 for i in range(N)]

A = np.array(A)

k = int(np.median(A))

ans = 0
for i in range(N):
    ans += abs(A[i] - k)

print(ans)