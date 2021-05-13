from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from math import gcd

a,b,c,d=nii()

a_c=(a-1)//c
b_c=b//c

a_d=(a-1)//d
b_d=b//d

lcm=(c*d)//gcd(c,d)
a_lcm=(a-1)//lcm
b_lcm=b//lcm

print((b-a+1)-(b_c-a_c)-(b_d-a_d)+(b_lcm-a_lcm))