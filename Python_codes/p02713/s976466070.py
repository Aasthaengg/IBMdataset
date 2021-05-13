import math
from functools import reduce

def gcd(*numbers) :
    return reduce(math.gcd , numbers)

K = int(input())
ans = 0
for i in range(1,K+1) :
    ans += i
for i in range(1,K) :
    for j in range(i+1,K+1) :
        ans += math.gcd(i,j) * 6
if K >= 3 :
    for i in range(1,K-1) :
        for j in range(i+1,K) :
            for k in range(j+1,K+1) :
                ans += gcd(i,j,k) * 6
print(ans)