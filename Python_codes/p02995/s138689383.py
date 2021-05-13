import math
A,B,C,D=map(int,input().split())
def X(x):
    c=x//C
    d=x//D
    l=C*D//math.gcd(C,D)
    return x-c-d+(x//l)
print(X(B)-X(A-1))