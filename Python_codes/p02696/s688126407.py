import math

A,B,N=map(int,input().split())

result=-1

x=min(B-1,N)
f1=math.floor(A*x/B)
f2=A*math.floor(x/B)
r=f1-f2
print(r)