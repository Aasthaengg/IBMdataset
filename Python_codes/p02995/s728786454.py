A, B, C, D = map(int, input().split())

cc = B // C - (A-1) // C
dd = B // D - (A-1) // D

import math
l = C * D // math.gcd(C, D)
cd = B // l - (A-1) // l

print(B - A + 1 - (cc + dd - cd))