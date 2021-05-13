import numpy as np

n= int(input())
a= [int(i) for i in input().split(' ')]

if abs(max(a)) >= abs(min(a)):
  ma  = max(a)
  ma_i= np.argmax(a)
  mi  = 0
  mi_i= 0
else:
  mi  = min(a)
  mi_i= np.argmin(a)
  ma  = 0
  ma_i= 0

xa=[]
if ma == 0:
  for i in range(n):
    if a[i] > 0:
      a[i] = a[i] + mi
      xa.append([mi_i+1, i+1])
  for i in reversed(range(1,n)):
    if a[i-1] > a[i]:
      a[i-1] = a[i-1] + a[i]
      xa.append([i+1, i-1+1])
else:
  for i in range(n):
    if a[i] < 0:
      a[i] = a[i] + ma
      xa.append([ma_i+1, i+1])
  for i in range(1,n):
    if a[i-1] > a[i]:
      a[i] = a[i] + a[i-1]
      xa.append([i-1+1,i+1])

print(len(xa))
for i in range(len(xa)):
  print(xa[i][0],xa[i][1])