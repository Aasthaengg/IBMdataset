import sys
sys.setrecursionlimit(10**6)
import math

n=int(input())
a=list(map(int,input().split()))

#print(a)

m=0
for i in range(n):
    while a[i]%2==0:
        m+=1
        a[i]=a[i]/2

print(m)

