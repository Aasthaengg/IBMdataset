import math
 
X = int(input())
 
for i in range(X, 100004):
  f = True
  for j in range(2, int(math.sqrt(X))+1):
    if i % j == 0:
      f = False
      break
  if f:
    print(i)
    break