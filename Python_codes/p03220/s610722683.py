import numpy as np
n = int(input())
temp0, avg = list(map(int, input().split(' ')))
height = list(map(int, input().split(' ')))

diff = [0]*n
for i in range(n):
  temp = temp0 - 0.006*height[i]
  diff[i] = abs(avg - temp)
print(np.argmin(diff)+1)
 

