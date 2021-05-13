from math import atan
from math import degrees
a,b,x=map(int,input().split())
X=x/a
if X>a*b/2:
    print(degrees(atan(2/a**2*(a*b-X))))
else:
    print(90-(degrees(atan(2*X/b**2))))