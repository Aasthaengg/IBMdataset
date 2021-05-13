import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

d1 = 0
for i in range(n):
    d1 += abs(x[i]-y[i])
print('{:.7f}'.format(d1))

d2 = 0
for i in range(n):
    d2 += abs(x[i]-y[i])**2
print('{:.7f}'.format(math.sqrt(d2)))

d3 = 0
for i in range(n):
    d3 += abs(x[i]-y[i])**3
print('{:.7f}'.format(d3**0.3333333333))

di = []
for i in range(n):
    di.append(abs(x[i]-y[i]))
print('{:.7f}'.format(max(di)))
