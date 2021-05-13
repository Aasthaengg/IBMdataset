import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

K = int(input())
ans = 0

for i in range(1,K+1):
    for j in range(i,K+1):
        for k in range(j,K+1):
            if i == j and j == k:
                ans += gcd(i,j,k)
            elif i != j and j != k and k!= i:
                ans += gcd(i,j,k)*6
            else:
                ans += gcd(i,j,k)*3
print(ans)