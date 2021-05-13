import math

n = int(input())
x = [float(x) for x in input().split()]
y = [float(y) for y in input().split()]
d = 0
for i in range(n):
    d += abs(x[i] - y[i])

print(d)

d = 0
for i in range(n):
    d += abs((x[i] - y[i])**2)

d = math.sqrt(d)
print(d)

d = 0
for i in range(n):
    d += abs((x[i] - y[i])**3)

d = math.pow(d, 1.0/3.0)
print(d)

d = 0
for i in range(n):
    if d <= abs(x[i] - y[i]):
        d = abs(x[i] - y[i])

print(d)