a, b = input().split()
ab = int(a+b)
import math
n = math.sqrt(ab)
if n % 1 == 0:
    print('Yes')
else:
    print('No')