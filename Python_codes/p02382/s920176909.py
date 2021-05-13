import math
n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))
a = 0
b = 0
c = 0
d = [0 for i in range(n)]
for i in range(n):
    a += abs(x[i]-y[i])
    b += abs(x[i]-y[i])**2
    c += abs(x[i]-y[i])**3
    d[i] = abs(x[i]-y[i])
b = math.sqrt(b)
c = c**(1/3)
print('{:.6f}'.format(a))
print('{:.6f}'.format(b))
print('{:.6f}'.format(c))
print('{:.6f}'.format(max(d)))
