import math

h = int(input())
w = int(input())
n = int(input())

l = max(h, w)
print(math.ceil(n / l))
