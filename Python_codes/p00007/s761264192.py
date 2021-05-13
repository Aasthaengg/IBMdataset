from math import ceil
a = 100
for i in range(input()):
    a *= 1.05
    a = ceil(a)
print int(a*1000)