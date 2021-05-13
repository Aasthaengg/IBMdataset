from math import gcd
n=int(input())
lc=int(input())
for i in range(n-1):
    t=int(input())
    gc=gcd(lc,t)
    lc=(t*lc)//gc
print(lc)    