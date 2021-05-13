import math
n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
ans=4
time=[a,b,c,d,e]
x=min(n,min(time))
print(ans+math.ceil(n/x))