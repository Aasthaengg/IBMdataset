import math

k=int(input())
n=0
for a in range(1,k+1):
    for b in range(1,k+1):
        d = math.gcd(a,b)
        for c in range(1,k+1):
            n+=math.gcd(d,c)
print(n)