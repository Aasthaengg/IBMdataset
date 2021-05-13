import math
n = int(input())
for i in range(n, 0, -1):
  if math.sqrt(i) == math.floor(math.sqrt(i)):
    print(i)
    break