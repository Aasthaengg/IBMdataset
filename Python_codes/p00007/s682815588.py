import math
n = input()

a = 100000
for i in range(n):
    a = 1.05 * a
    a /= 1000
    a = int(math.ceil(a) * 1000)
print (a)