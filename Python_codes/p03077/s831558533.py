import math


n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

f = min(a, b, c, d, e)
ans = (math.ceil(n / f) - 1) + 5
print(ans)
