import math
A, B, C, D = map(int, input().split())
cdiv = B // C - (A - 1) // C
ddiv = B // D - (A - 1) // D
lcm = (C * D) // math.gcd(C, D)
cddiv = B // lcm - (A - 1) // lcm
ans = (B - A + 1) - (cdiv + ddiv - cddiv)
print(ans)