from math import gcd 
a,b,c=map(int,input().split())
if gcd(a,b)==1:
    print("YES")
else:
    g=gcd(a,b)
    print("YES" if c%g==0 else "NO")
    

