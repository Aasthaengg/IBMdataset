import math

A, B, X = map(int, input().split())
if A * A * B < 2 * X:
    print(math.degrees(math.atan(2 * B / A - 2 * X / A ** 3)))
else:
    print(math.degrees(math.atan(A * B * B / (2 * X))))
