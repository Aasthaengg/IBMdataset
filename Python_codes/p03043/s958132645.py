from fractions import Fraction
import math
n,k=list(map(int,input().split()))
ans=0
for i in range(1,n+1):
    if i>=k:
        ans+=(Fraction(1,n))
    else:
        x=int(math.log((k/i),2))
        if (k/i)%(2**x)!=0:
            x+=1
        ans+=Fraction(1,n*(2**x))
print(float(ans))