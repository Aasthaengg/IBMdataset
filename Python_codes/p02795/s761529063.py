import math
h = int(input())
w = int(input())
n = int(input())
a = n / max(h, w)
a = math.ceil(a)
print(a)