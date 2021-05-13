import math
a,b,c,d=map(int,input().split())
lcm=c*d//math.gcd(c,d)
a1,a2,a3=(a-1)//c,(a-1)//d,(a-1)//lcm
b1,b2,b3=b//c,b//d,b//lcm
ans=b-a+1-(b1+b2-b3-a1-a2+a3)
print(ans)
