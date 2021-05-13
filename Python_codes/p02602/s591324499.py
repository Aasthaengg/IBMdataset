import numpy as np
n, k = map(int, input().split())
A = list(map(int, input().split()))
A = np.array(A)

for i in range(n-k):
  if A[k+i] > A[i]:
    print("Yes")
  else:
    print("No")
