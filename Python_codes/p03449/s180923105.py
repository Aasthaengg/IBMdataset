import numpy as np
n = int(input())
ans = np.zeros(n)
base = []
for i in range(2):
  base.append(list(map(int,input().split())))

ans[0] = base[0][0]
for i in range(n):
  ans[0] += base[1][i]
  
for i in range(1,n):
  ans[i] = ans[i-1] - base[1][i-1] + base[0][i]
  
print(int(np.max(ans)))