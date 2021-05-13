import numpy as np

n = int(input())
even_count = [0 for i in range(n)]
for i in range(1,n+1):
  j = i
  count = 0
  while True:
    if i % 2 == 0:
      count += 1
      i = int(i / 2)
    else:
      break
  even_count[j-1] = count
print(np.argmax(even_count)+1)