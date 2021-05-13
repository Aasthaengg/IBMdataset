from math import ceil
n = int(input())
d = 100000
c = 1000
for i in range(n):
    d *= 1.05
    d =int(ceil(d/c))*c
print(d)