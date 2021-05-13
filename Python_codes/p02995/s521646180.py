import math
A,B,C,D=map(int,input().split())

E = C*D//math.gcd(C,D)
all = B - A + 1
Cmod = B//C - (A-1)//C
Dmod = B//D - (A-1)//D
CDmod = B//E - (A-1)//E

print(all - Cmod - Dmod + CDmod)