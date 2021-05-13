import math
(a, b, C) = [int(i) for i in input().split()]
radC = math.radians(C)
h = b * math.sin(radC)
S = (a * h) / 2
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(radC))
print('{0:.4f}\n{1:.4f}\n{2:.4f}'.format(S,L,h))