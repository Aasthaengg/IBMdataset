k=int(input())
t=0
import math
for i in range(1,k+1):
    for j in range(1,k+1):
        s=math.gcd(i,j)
        for l in range(1,k+1):
            S=math.gcd(s,l)
            t+=S
print(t)