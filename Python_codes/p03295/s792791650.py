import numpy as np

N, M =  map(int, input().split())
X = np.zeros([M,2], dtype=int)

for i in range(M):
    X[i,0], X[i,1] = map(int, input().split())

col_num = 1
X = X[np.argsort(X[:, col_num])]
cnt = 1
r_min = X[0,1]
for i in range(1,M):
    if X[i,0] >= r_min:
        cnt += 1
        r_min = X[i,1]
print(cnt)