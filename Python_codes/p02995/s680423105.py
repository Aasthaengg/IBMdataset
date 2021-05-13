import math
A, B, C, D = map(int, input().split())
L = C * D //math.gcd(C, D)
x = (A - 1) - (A -1) // C - (A - 1) // D + (A - 1) //L
y = B - B // C - B // D + B // L
print(y - x)