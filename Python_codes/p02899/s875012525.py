import numpy as np
N = int(input())
A = list(map(int, input().split()))
ans = np.zeros(N)
for i in range(N):
  ans[A[i]-1] = i + 1
  
ans = list(map(int, ans))
ans = list(map(str, ans))
print(" ".join(ans))