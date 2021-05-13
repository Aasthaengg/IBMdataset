import math
X = int(input())
temp = int(math.sqrt(X))
while True:
  b = True
  for i in range(2, temp + 1):
    if X % i == 0:
      b = False
      break
  if b == True:
    print(X)
    exit()
  X += 1