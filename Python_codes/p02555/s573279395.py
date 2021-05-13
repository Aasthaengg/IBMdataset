import numpy as np
from functools import reduce


mod = 10**9+7
def cmb(R,B):
    numerator = reduce(lambda x,y: x * y % mod, [R+B-k for k in range(B)])
    denominator = reduce(lambda x, y: x * y % mod, [B-k for k in range(B)])
    return numerator * pow(denominator, mod - 2, mod) % mod


S = int(input())
p = S // 3
A = 0

for b in range(p):

    r = S-3*(b+1)

    if b == 0:
        A+=1
    else:
        A+=cmb(r,b)

print(A%mod)



