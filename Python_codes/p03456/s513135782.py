import math
a, b = input().split()
ab = int(a+b)
if int(math.sqrt(ab))**2 == ab:
    print('Yes')
else:
    print('No')