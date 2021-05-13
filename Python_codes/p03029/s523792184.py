import math
A, P = map(int, input().split())
pie = 0.5 * (P + 3 * A)
realPie = math.floor(pie)
print(realPie)