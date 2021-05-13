import math
K=int(input())
num=0
for h in range(1,K+1):
    for i in range(1,K+1):
        ans=math.gcd(h,i)
        for j in range(1,K+1):
            num+=math.gcd(ans,j)

print(num)
