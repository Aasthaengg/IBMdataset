import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

K = int(input())

sum = 0

for a in range(1,K+1):
    for b in range(a,K+1):
        for c in range(b,K+1):
            if a == b == c:
                sum += gcd(a,b,c)
            elif a == b or b == c:
                sum += gcd(a,b,c) * 3
            else:
                sum += gcd(a,b,c) * 6
print(sum)
