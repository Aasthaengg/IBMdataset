n,m = map(int,input().split())

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if (n>1)&(m>1):
	print(combinations_count(n, 2)+combinations_count(m, 2))
elif n>1:
    print(combinations_count(n, 2))
elif m>1:
    print(combinations_count(m, 2))
else:
    print(0)