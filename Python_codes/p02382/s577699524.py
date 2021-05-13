import math
n = int(raw_input())
x = []
y = []
# input part
in_line = raw_input().split()
for i in range(n):
    x.append(float(in_line[i]))
in_line = raw_input().split()
for i in range(n):
    y.append(float(in_line[i]))
# output part
# p=1
d = 0.0
for i in range(n):
    d += math.fabs(x[i]-y[i])
print d
# p=2
d = 0.0
for i in range(n):
    d += math.fabs(x[i]-y[i])**2
print math.sqrt(d)
# p=3
d = 0.0
for i in range(n):
    d += math.fabs(x[i]-y[i])**3
print d**(1.0/3.0)
# p=inf
d = 0.0
for i in range(n):
    if d < math.fabs(x[i]-y[i]):
        d = math.fabs(x[i]-y[i])
print d