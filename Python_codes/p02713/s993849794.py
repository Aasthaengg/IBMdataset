K = int(input())
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)


temp = []

for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            temp.append(gcd(i,j,k))
print(sum(temp))