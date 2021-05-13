import math
A,B,C,D=map(int,input().split())
A-=1
E=(C*D)//math.gcd(C,D)
print(B-A-(B//C+B//D-B//(E)-(A//C+A//D-A//(E))))