import math


k = int(input())
ans = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        tmp = math.gcd(i,j)
        for x in range(1,k+1):
            ans +=math.gcd(tmp,x) 

            
print(ans)
