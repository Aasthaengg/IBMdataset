from itertools import product
import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))

cnt = 0
for x in list(product([-1, 0, 1], repeat=n)):
  temp = a.copy() - np.array(x)
  if np.prod(temp) % 2 == 0:
    cnt+=1
print(cnt)
  

