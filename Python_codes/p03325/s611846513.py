import numpy as np
 
n = int(input())
a =list(map(int, input().split()))
b = 0
for i in range(n):
  for j in range(30):
    if(a[i]%2==0):
      a[i] = a[i]/2
      b+=1
    else:
      break
print(b)