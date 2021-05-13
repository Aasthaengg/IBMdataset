a,b,c = map(int, input().split())

import math
# if round(math.sqrt(a) + math.sqrt(b), 10) < round(math.sqrt(c), 10):
# if abs(math.sqrt(a) + math.sqrt(b) - math.sqrt(c)) < 1e-10:
if c - a - b > 0 and 4 * a * b < (c-a-b)*(c-a-b):
    print("Yes")
else:
    print("No")