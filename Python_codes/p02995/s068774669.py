import math

A, B, C ,D = map(int, input().split())


C_multiple = B // C - A // C
D_multiple = B // D - A // D 

if A % C == 0:
    C_multiple += 1
if A % D == 0:
    D_multiple += 1
        

CD_gcd = C * D // math.gcd(C,D) 
CD_multiple = B // CD_gcd - A// CD_gcd 
if A % CD_gcd == 0:
    CD_multiple += 1



ans = ( B - A + 1 ) - (C_multiple + D_multiple - CD_multiple)
print(int(ans))