import math
X = [int(input()) for _ in range(5)]
t = 0
m = 100
for x in X:
  t += (math.ceil(x/10))*10
  if x%10 != 0:
    m = min(m, x%10)
print(t+m-10 if m!=100 else t)