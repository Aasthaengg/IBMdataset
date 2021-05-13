# coding:utf-8
import math
n = input()
x = map(float, raw_input().split())
y = map(float, raw_input().split())
d1 = 0.0
d2 = 0.0
d3 = 0.0
d4 = 0.0
for i in range(n):
    d1 += abs(x[i] - y[i])
    d2 += pow(abs(x[i] - y[i]),2)
    d3 += pow(abs(x[i] - y[i]),3)
    d4 = max(d4,abs(x[i] - y[i]))
d2 = math.sqrt(d2)
d3 = d3 ** (1.0 / 3.0)
print d1
print d2
print d3
print d4

