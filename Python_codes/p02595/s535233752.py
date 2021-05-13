import numpy as np
n,d = map(int,input().split())
s = 0
for i in range(n):
  x,y = map(int,input().split())
  D = np.sqrt(x**2+y**2)
  if d >= D:
    s += 1
    
print(s)    