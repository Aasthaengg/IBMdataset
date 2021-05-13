import math

A,B,C,D = map(int, input().split())
E = C*D // math.gcd(C, D)
count =0
n = (A-1)//C
m = B//C
o = (A-1)//D
p= B//D
q= (A-1)//E
r= B//E
print((B-A+1) - ((m-n)+(p-o)-(r-q)))