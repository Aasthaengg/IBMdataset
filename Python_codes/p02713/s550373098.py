import math
k=int(input())
ans=0
gcd1=[0]*200
for i in range(1,k+1):
    for j in range(1,k+1):
        gcd1[math.gcd(i,j)-1]+=1


for i in range(1,k+1):
    for j in range(1,k+1):
        if gcd1[j-1]>=1:
            ans+=math.gcd(j,i)*gcd1[j-1]

print(ans)