import math
k = int(input())

sm=0
for i in range(1,k+1):
    for l in range(1,k+1):
        gcdab=math.gcd(i,l)
        for m in range(1,k+1):
            sm+=math.gcd(gcdab,m)

print(sm)