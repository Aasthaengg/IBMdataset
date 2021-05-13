import math
A, B, C, D = list(map(lambda x: int(x), input().split(" ")))
print("Yes") if math.ceil(A/D) >= math.ceil(C/B) else print("No")