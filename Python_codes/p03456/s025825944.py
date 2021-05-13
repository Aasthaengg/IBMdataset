import math
a, b = input().split()
n =int( a + b )
if int( n ** 0.5 ) ** 2 == n:
    print('Yes')
else:
    print('No')
