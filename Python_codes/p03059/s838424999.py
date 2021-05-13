import math
a, b, t = map(int, input().split())
print(math.floor(t + 0.5) // a * b)