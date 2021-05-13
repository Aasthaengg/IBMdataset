import math
A, B, X = list(map(int, input().split()))
if X >= (A**2)*B / 2:
    print(math.degrees(math.atan2(2*((A**2)*B - X), A**3)))
else:
    print(math.degrees(math.atan2(A*B*B, 2 * X)))