import math
A, B, C, D = map(int, input().split())

t = math.ceil(C / B)
a = math.ceil(A / D)

print('Yes' if t <= a else 'No')
