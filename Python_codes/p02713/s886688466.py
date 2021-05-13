from math import gcd
K=int(input())
s=0
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            s+=gcd(gcd(i,j),k)
print(s)        