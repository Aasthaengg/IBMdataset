from math import gcd

def lcm(a,b):
    return (a//gcd(a,b))*b

def f(x,p):
    return x//p

A,B,C,D=map(int,input().split())
E=lcm(C,D)

X=f(B,C)-f(A-1,C)
Y=f(B,D)-f(A-1,D)
Z=f(B,E)-f(A-1,E)
print(B-A+1-(X+Y-Z))
