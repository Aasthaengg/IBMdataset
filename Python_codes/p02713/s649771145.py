import functools
import math

K = int(input())

def gcd_2(*vals):
    return functools.reduce(math.gcd, vals)

ans=0
for x in range(1,K+1):
    for y in range(1,K+1):
        for z in range(1,K+1):
            ans += gcd_2(x,y,z)

print(ans)
