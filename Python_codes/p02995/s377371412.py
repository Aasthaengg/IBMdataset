import math
A, B, C, D = map(int, input().split())
c = B // C - A // C + int(A % C == 0)
d = B // D - A // D + int(A % D == 0)
E = int((C * D) / math.gcd(C, D))
e = B // E - A // E + int(A % E == 0)
print(B - A + 1 - c - d + e)