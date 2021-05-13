A, B, C, D = list(map(int, input().split()))
c1 = (A - 1) // C
c2 = B // C
d1 = (A - 1) // D
d2 = B //D
import math
E = (C * D) // math.gcd(C, D)
e1 = (A - 1) // E
e2 = B //E

print(B - A + 1 -(c2 - c1 + d2 - d1 - (e2 - e1)))
