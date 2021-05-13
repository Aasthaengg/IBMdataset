import math

x=int(input())
G=math.gcd(x,360)
L=x*360//G
ans=L//x
print(ans)
