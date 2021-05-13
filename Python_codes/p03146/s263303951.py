import numpy as np
s = int(input())

ans = np.zeros(1000000)
a = s
ans[a] += 1
for i in range(1,1000000):
  if a % 2 == 0:
    a =  a//2
    ans[a] += 1
  else:
    a = 3*a+1
    ans[a] += 1
  if ans[a] == 2:
    print(i+1)
    break