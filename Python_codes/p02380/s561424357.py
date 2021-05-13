import math
a, b ,angleC = [float(x) for x in input().split(" ")]

c = math.sqrt((a **2) + (b **2) - 2*a*b*(math.cos(math.radians(int(angleC))) ))

S = 1/2 * a * b * (math.sin(math.radians(int(angleC))))
L = a + b + c
h = 2 * S / a


print(S)
print(L)
print(h)