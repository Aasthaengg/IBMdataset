from math import gcd
def lcm(a, b):
    return a*b//gcd(a, b) 

A, B, C, D = map(int,input().split())
As = [(A-1)//C, (A-1)//D, (A-1)//lcm(C,D)]
Bs = [B//C, B//D, B//lcm(C,D)]

aa = (A-1) - (As[0]+As[1]-As[2])
bb = B - (Bs[0]+Bs[1]-Bs[2])

print(bb-aa)