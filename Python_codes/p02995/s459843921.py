import math

A,B,C,D=map(int,input().split())
g=(C*D)//math.gcd(C,D)
print((B-A+1)-(B//C--(-A//C)+1)-(B//D--(-A//D)+1)+(B//g--(-A//g)+1))