import numpy as np
n,k = map(int,input().split())
m = 10**9 + 7
gcds = np.zeros(k+1, int)

for i in range(k,0,-1):
  tmp = k // i
  gcds[i] = pow(tmp,n, m)
  for j in range(tmp,1,-1):
    gcds[i] -= gcds[j*i]
ans = 0
for i in range(k,0,-1):
  ans = (ans + gcds[i]*i)%m
print(ans)