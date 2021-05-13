import math
a, b, x = map(float, input().split())
s = a * b * math.sin(math.radians(x)) / 2
l = a + b + math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(x)))
h = b * math.sin(math.radians(x))
print('%f' % s)
print('%f' % l)
print('%f' % h)
