from math import gcd

K = int(input())
sum = 0

for i in range(1,K+1):
    for j in range(1,K+1):
        A = gcd(i,j)
        for k in range(1,K+1):
            sum += gcd(A,k)
    
print(sum)