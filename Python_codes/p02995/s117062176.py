import math
A, B, C, D = map(int, input().split())
L = C*D//(math.gcd(C, D))
C_div = B//C-(A-1)//C
D_div = B//D-(A-1)//D
L_div = B//L-(A-1)//L
print(B-A+1-(C_div+D_div-L_div))