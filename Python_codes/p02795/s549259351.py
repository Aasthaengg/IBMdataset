import math
h = int(input())
w = int(input())
n = int(input())

m = max(h,w)
print(math.ceil(n/m))
