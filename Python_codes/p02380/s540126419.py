import math

a, b, c = list(map(int, input().split()))

pc = math.pi * c / 180
s = a * b * math.sin(pc) / 2
l = a + b + math.sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b * math.cos(pc))
h = s / a * 2
print(s)
print(l)
print(h)

