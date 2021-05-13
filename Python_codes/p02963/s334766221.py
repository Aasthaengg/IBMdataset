import math
S = int(input())
a = math.ceil(math.sqrt(S))
b = a ** 2 - S
a2 = str(a)
b2 = str(b)
print("0 0 " + a2 + " 1 " + b2 + " " + a2)