from math import *
n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=len(a)-len(b)
k=ceil(c/2)
print(len(a)-2*k)