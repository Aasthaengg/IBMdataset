import math

A, B, C, D = map(int, input().split())

b = B - ((B // C) + (B // D) - (B // (C*D // math.gcd(C,D)))) 
a = A-1 - (((A-1) // C) + ((A-1) // D) - ((A-1) // (C*D // math.gcd(C,D))))
res = b - a
print(res)