import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

A,B,C,D = list(map(int,input().split()))
if A%C == 0:
    num_C_bai = (B-(B%C) - A)//C + 1
else:
    num_C_bai = ((B-(B%C) - (A-(A%C)+C)))//C + 1
    
if A%D == 0:
    num_D_bai = (B-(B%D) - A)//D + 1
else:
    num_D_bai = ((B-(B%D) - (A-(A%D)+D)))//D + 1

E = lcm(C,D)

if A%E == 0:
    num_E_bai = (B-(B%E) - A)//E + 1
else:
    num_E_bai = ((B-(B%E) - (A-(A%E)+E)))//E + 1

print(B + 1 - A - num_C_bai - num_D_bai + num_E_bai)
