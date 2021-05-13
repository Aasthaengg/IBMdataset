from math import gcd
k = int(input())
res = 0

for i in range(1,k+1):
    for j in range(1,k+1):
        for k in range(1,k+1):
            res += gcd(gcd(i,j),k)
print(res)
