K=int(input())
import math

sum=0

sum+=K*(K+1)//2

for i in range(1,K+1):
    for j in range(1,K+1):
        if j<=i:
            continue
        else:
            sum+=6*math.gcd(i,j)

for i in range(1,K+1):
    for j in range(1,K+1):
        if j<=i:
            continue
        else:
            for k in range(1,K+1):
                if k<=j:
                    continue
                else:
                    sum+=6*math.gcd(math.gcd(i,j),k)

print(sum)