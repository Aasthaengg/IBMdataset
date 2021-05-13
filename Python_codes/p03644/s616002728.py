import numpy as np
n = int(input())
array = [0]*n

for i in range(1, n+1):
  count = 0
  num = i
  while num%2==0:
    count += 1
    num = int(num/2)
  array[i-1] = count
print(1+np.argmax(array))
