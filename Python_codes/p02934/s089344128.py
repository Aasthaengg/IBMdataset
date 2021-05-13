import sys
from fractions import gcd
N=int(sys.stdin.readline().strip())
A=map(int, sys.stdin.readline().split())
for i,a in enumerate(A):
    if i==0:
        a_gcd=a
    else:
        a_gcd=gcd(a_gcd,a)

a_lcm=a_gcd
for a in A:
    a_lcm*=a/a_gcd

bunbo=0
for a in A:
    bunbo+=a_lcm/a

print float(a_lcm)/bunbo