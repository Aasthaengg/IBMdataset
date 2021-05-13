import math
K=int(input())
ans=0
for h in range(1,K+1):
    for i in range(1,K+1):
        gcd=math.gcd(h,i)
        if gcd==1:
            ans+=K
        else:
            for j in range(1,K+1):
                ans+=math.gcd(gcd,j)
print(ans)