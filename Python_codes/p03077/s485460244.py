import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


minmove = min([a, b, c, d, e])

ans = math.ceil(n/minmove) + 4

print(ans)