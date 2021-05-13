import math

def lcm(a,b):
    return a//math.gcd(a,b)*b

A,B,C,D=map(int,input().split())

def calc(N):
    return N-N//C-N//D+N//lcm(C,D)

print(calc(B)-calc(A-1))

