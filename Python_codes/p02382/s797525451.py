import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
d1 = 0
d2 = 0
d3 = 0
dmax = 0
for i in range(n):
  d1 += abs(x[i] - y[i])
  d2 += abs(x[i] - y[i])**2
  d3 += abs(x[i] - y[i])**3
  if dmax < abs(x[i] - y[i]):
    dmax = abs(x[i] - y[i])
print(d1)
print(math.sqrt(d2))
print(d3**(1.0/3.0))
print(dmax)
