import math
A, B, C, D = map(int, input().split())
total = B-A+1
A -= 1
waruC = (B//C)-(A//C)
waruD = (B//D)-(A//D)
CD = C * D // math.gcd(C, D)
waruCD = (B//CD)-(A//CD)
print(total-waruC-waruD+waruCD)
