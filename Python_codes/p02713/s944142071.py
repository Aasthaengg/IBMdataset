import math
from math import gcd

K = int(input())
result = 0

for i in range(1, K+1):
    result += i

for i in range(1, K):
    for j in range(i+1, K+1):
        result += gcd(i,j) * 6

if K >= 3:
    for i in range(1, K-1):
        for j in range(i+1, K):
            for k in range(j+1, K+1):
                result += gcd(gcd(i,j),k) * 6

print(result)