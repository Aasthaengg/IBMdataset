import numpy as np
N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))
right = 0
left = 0
ans = 0
for i in range(N):
  right += ((A[i+1:] < A[i]).sum())
  left += ((A[:i] < A[i]).sum())
ans += K*(K+1)//2 % (10**9+7) * right
ans += (K-1)*K//2 % (10**9+7) * left
ans = ans % (10**9+7) 
print(ans)