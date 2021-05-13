import math
from decimal import Decimal
A, B, H, M = map(int, input().split())
theta = abs(11/2*M - 30*H)
rad = math.radians(theta)
cos = Decimal(math.cos(rad))
ans = math.sqrt(A**2 + B**2 - 2 * A * B * cos)
print("{:.020f}".format(ans))