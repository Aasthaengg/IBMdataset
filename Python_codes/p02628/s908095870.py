import numpy as np

N, K = map(int, input().split())
A = [int(i) for i in input().rstrip().split()]
A.sort()

B = A[0:K]
ans = np.sum(B)
print(ans)