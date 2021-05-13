import numpy as np

N, M, X = map(int, input().split())

C = []
A = []
for _ in range(N):
    inp = list(map(int, input().split()))
    C.append(inp[0])
    A.append(inp[1:])
A = np.array(A)

for i in range(M):
    if np.sum(A, axis=0)[i] < X:
        print(-1)
        exit()

min_c = 999999999999999
for i in range(2**N):
    item = []
    tmp_c = 0
    for j in range(N):
        if ((i >> j) & 1):
            item.append(A[j])
            tmp_c += C[j]
    if len(item) == 0:
        continue
    for j in range(M):
        if np.sum(item, axis=0)[j] < X:
            break
        if j == M-1:
            if min_c > tmp_c:
                min_c = tmp_c

print(min_c)
