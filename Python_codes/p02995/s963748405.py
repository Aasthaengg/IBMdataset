import math
A,B,C,D = map(int,input().split())
f1 = (A-1)-((A-1)//C+(A-1)//D-(A-1)//(C*D//math.gcd(C,D)))
f2 = (B)-((B)//C+(B)//D-(B)//(C*D//math.gcd(C,D)))
print(f2-f1)