import numpy as np
w,h,n = map(int, input().split())
area = np.array([[1]*w]*h)

for _ in range(n):
  x,y,a = map(int, input().split())
  if a == 1:
    area[:,:x]=0
  elif a == 2:
    area[:,x:]=0
  elif a == 3:
    area[:y,:]=0
  elif a == 4:
    area[y:,:]=0
print(area.sum())