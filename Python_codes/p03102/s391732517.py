import numpy as np

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

B_array = np.array(B)
A_array = np.array(A)

count = 0
for i in range(N):
    code = (A_array[i, :] * B_array).sum() + C

    if code > 0:
        count += 1

print(count)