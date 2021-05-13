a, b, c, d = map(int, input().split())
import math
ab = math.sqrt(abs(a - b) ** 2)
bc = math.sqrt(abs(b - c) ** 2)
ac = math.sqrt(abs(a - c) ** 2)

print("Yes" if ac<=d or ab<=d and bc<=d else "No")