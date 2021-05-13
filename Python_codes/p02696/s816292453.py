import math

A,B,N=map(int,input().split())

x=min(B-1,N)
f1=math.floor(A*x/B)
f2=A*math.floor(x/B)
result=f1-f2
print(result)