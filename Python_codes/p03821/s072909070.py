import numpy as np

N = int(input())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A = np.array(A[::-1])
B = np.array(B[::-1])

ans = 0

# print(A, B)

for i in range(N):
    m = A[i] % B[i]
    if m == 0:
        continue
    else:
        if i != N - 1:
            A[i + 1 :] += B[i] - m
        # print(i, B[i] - m)
        ans += B[i] - m


print(ans)

