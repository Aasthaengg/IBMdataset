n = int(input())
c = 1
t = 1
while t <= n:
  c = (c*t)%(10**9+7)
  t += 1
print(c)