import math
L, R, D = map(int, input().split())

print(math.floor(R / D) - math.ceil(L / D) + 1)

