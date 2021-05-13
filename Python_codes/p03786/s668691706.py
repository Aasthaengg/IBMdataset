import numpy as np
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
a = np.array(a)
c = np.array([0]*n)
np.cumsum(a,out=c)
ans = n
for i in range(n-1,0,-1):
  if c[i-1]*2 < a[i]:
    ans -= i
    break
print(ans)