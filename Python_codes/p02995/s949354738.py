import math

A, B, C, D = map(int, input().split())

lcm = C * (D // math.gcd(C, D))

cntA = (A - 1) // C + (A - 1) // D - (A - 1) // lcm
cntB = B // C + B // D - B // lcm
ans = B - A + 1 - (cntB - cntA)
print(ans)