import math
A,B,C,D = map(int,input().split())

def lcm(a,b):
    return a*b // math.gcd(a,b)

x = [(A-1)//C,(A-1)//D,(A-1)//lcm(C,D)]
y = [B // C,B//D,B//lcm(C,D)]

an = (A-1) - (x[0]+x[1]-x[2])
bn =  B - (y[0]+y[1]-y[2])

print(bn-an)