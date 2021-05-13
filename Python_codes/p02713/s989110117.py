import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

n = int(input()) + 1
ans = 0
for i in range(1,n):
    for j in range(1,i+1):
        for k in range(1,j+1):
            if i == j == k:
                m = 1
            elif i == j or j == k or k == i:
                m = 3
            else:
                m = 6
            a = [i,j,k]
            ans += gcd_list(a) * m
print(ans)