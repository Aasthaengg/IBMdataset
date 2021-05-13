n=int(input())
import math
res=0
for a in range(1,n+1):
    for b in range(1, n + 1):
        gcd1 = math.gcd(a, b)
        for c in range(1, n + 1):
           gcd2=math.gcd(gcd1,c)
           res+=gcd2
print(res)