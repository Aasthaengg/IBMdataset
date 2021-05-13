import math
a, b = input().split()
print("Yes" if math.sqrt(int(a + b)).is_integer() else "No")