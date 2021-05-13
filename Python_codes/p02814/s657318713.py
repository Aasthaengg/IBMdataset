import fractions
import numpy as np

N, M = map(int,input().split())
A = list(map(int,input().split()))

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

bef = 1
LCM = 1
ans = []
for i,a in enumerate(A):
    LCM = lcm(LCM,a)
    if bef !=1:
        c, d = bef, a//2
        while c % 2 == 0 and d % 2 == 0:
            c //= 2
            d //= 2
        if c%2 != d%2:
            print(0)
            exit()
    
    b = a//2
    bef = lcm(bef,b)
    ans.append(bef)

print((M-bef)//LCM+1)