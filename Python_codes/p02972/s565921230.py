import numpy as np
n = int(input())
A = np.fromstring(input(), dtype=np.int32, sep=' ')
T = np.zeros(n, dtype=np.int32)

ans = []
for i in range(n-1, -1, -1):
  x = A[i]^np.logical_xor.reduce(T[i:n:i+1])
  if x:
    T[i] = 1
    ans.append(i+1)

print(len(ans))
print(*ans)