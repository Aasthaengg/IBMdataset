from math import *
n=int(input())
l=list(map(int,input().split()))
g=l[0]
for i in range(1,n):
    g=gcd(g,l[i])
print(g)