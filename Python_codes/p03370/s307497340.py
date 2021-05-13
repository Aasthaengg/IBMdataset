import numpy as np

n, x = map(int, input().split())
m = np.zeros(n)
x_sum = 0

for i in range(n):
  m[i] = int(input())
  x_sum += m[i]
  
print(int((x - x_sum) / np.min(m)) + n)
