#C
import math
K =int(input())
ans=0
for i in range(1, K+1):
    for j in range(1, K+1):
        tmp_gcd=math.gcd(i,j)
        for k in range(1, K+1):
            ans+=math.gcd(tmp_gcd, k)
print(ans)