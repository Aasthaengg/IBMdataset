import numpy as np
# 締切が早いものから処理
N = int(input())
AB = np.array([[int(x) for x in input().split()] for _ in range(N)])
A = AB[:,0]
B = AB[:,1]
idx = B.argsort()
A = A[idx]
B = B[idx]
np.cumsum(A, out = A)
bl = (A <= B).all()
answer = 'Yes' if bl else 'No'
print(answer)
