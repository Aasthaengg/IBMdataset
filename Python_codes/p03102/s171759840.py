import numpy as np

N, M, C = map(int, input().split())
B = np.array(list(map(int, input().split())))
A = np.array([tuple(map(int, input().split())) for _ in range(N)])

cnt = 0
for i in range(N):
    if sum(B * A[i]) + C > 0:
        cnt += 1
print(cnt)

