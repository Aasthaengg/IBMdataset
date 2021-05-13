from math import atan2, degrees

A, B, X = map(int, input().split())
if A ** 2 * B > X * 2:
    width = X * 2 / (A * B)
    print(degrees(atan2(B, width)))
else:
    height = (A ** 2 * B - X) * 2 / (A ** 2)
    print(degrees(atan2(height, A)))
