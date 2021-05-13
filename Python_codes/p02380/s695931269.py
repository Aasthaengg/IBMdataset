import math
a, b, c = map(int, input().split())

S = a * b * math.sin(math.radians(c)) / 2
cl = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(c)))
L = a + b + cl
h = S*2/a

print('{:.4f}'.format(S))
print('{:.4f}'.format(L))
print('{:.4f}'.format(h))
