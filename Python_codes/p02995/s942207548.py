import math
A,B,C,D = (int(x) for x in input().split())
Num = B-A+1
Dup = C*D//math.gcd(C,D)
MinC  = (A+(C-A%C)%C)//C
MinD  = (A+(D-A%D)%D)//D
MinCD = (A+(Dup-A%Dup)%Dup)//Dup
OvrC  = (B+(C-B%C)%C)//C + (B%C==0)
OvrD  = (B+(D-B%D)%D)//D + (B%D==0)
OvrCD = (B+(Dup-B%Dup)%Dup)//Dup + (B%Dup==0)
CDNum = (OvrC-MinC)+(OvrD-MinD)-(OvrCD-MinCD)
print(Num-CDNum)