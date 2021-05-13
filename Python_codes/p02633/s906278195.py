X=int(input())
from math import*
ans=X*360//gcd(X,360)//X
print(ans)