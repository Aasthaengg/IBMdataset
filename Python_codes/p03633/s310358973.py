import math

def lcm(x,y):
    return (x*y)//math.gcd(x,y)

n=int(input())
t=[int(input()) for i in range(n)]

LCM=t[0]
for i in range(1,n):
    LCM=lcm(LCM,t[i])

print(LCM)