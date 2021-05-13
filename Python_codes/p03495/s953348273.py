import numpy as np
n,k = map(int,input().split())
a = list(map(int,input().split()))

base = np.zeros(n)
for i in range(n):
  base[a[i]-1] += 1
  
seen = np.where(base>0,1,0)
num = np.sum(seen) - k

if num <= 0:
  ans = 0
elif num > 0:
  base.sort()
  count = 0
  ans = 0
  for i in range(n):
    if base[i] != 0:
      ans += base[i]
      count += 1
      
    if count == num:
      break
    
print(int(ans))