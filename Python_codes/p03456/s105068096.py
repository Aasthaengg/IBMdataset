import math
a, b = input().split()

i = math.sqrt(int(a + b))

if i.is_integer() == True:
    print('Yes')
else:
    print('No')
