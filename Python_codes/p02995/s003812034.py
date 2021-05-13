from math import *

A,B,C,D=map(int,input().split())
mc=B//C-(A-1)//C
md=B//D-(A-1)//D
cd=(C*D)//gcd(C,D)
mcd=B//cd-(A-1)//cd
print(B-A+1-mc-md+mcd)
