import math
n = input()
x = map(int, raw_input().split())
y = map(int, raw_input().split())
print sum([abs(x[i]-y[i]) for i in range(len(x))])
print math.sqrt(sum([(x[i] - y[i])**2 for i in range(len(x))]))
print pow(sum([abs(x[i] - y[i])**3 for i in range(len(x))]), 1/3.0)
print max([abs(x[i]-y[i]) for i in range(len(x))])