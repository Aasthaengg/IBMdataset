import math
 
a, b, x = list(map(int, input().split()))
c = 2 * x / a / b
if c > a:
    bt = 2 * (b - x / a / a)
    print(math.degrees(math.atan2(bt, a)))
else:
    print(math.degrees(math.atan2(b, c)))