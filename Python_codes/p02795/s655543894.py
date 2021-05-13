import math
h = int(input())
w = int(input())
n = int(input())

t = max(h,w)
print(math.ceil(n/t))
