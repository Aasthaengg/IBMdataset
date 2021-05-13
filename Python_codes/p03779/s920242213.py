import math
X = int(input())
m = math.sqrt(X * 2)
t = 0
for i in range(1, math.ceil(m) + 1):
  t += i
  if t >= X:
    print(i)
    exit()