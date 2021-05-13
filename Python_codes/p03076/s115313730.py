import math
t = []
for i in range(5):
  t.append(int(input()))

u = list(map(lambda s: math.ceil(s/10) * 10, t))
z = [b - a for (a, b) in zip(t, u)]
print(sum(u) - max(z))