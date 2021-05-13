n,m = map(int,input().split())
a = list(map(int,input().split()))

import math
lcm = 1
for i in range(n):
    b = a[i]//2
    lcm = lcm*b //math.gcd(lcm,b)
if any(2*lcm//i % 2 == 0 for i in a):
    print(0)
else:
    print((m-lcm)//(2*lcm) + 1)