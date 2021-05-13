import math
H = int(input())
a = int(math.log2(H))
b = 2 ** a
print(b * 2 - 1)