import math
a,b=map(int,input().split())
A=math.factorial(a)
B=math.factorial(b)
m=10**9+7
if abs(a-b)<=1:
    if a==b:
        print(2*A*B%m)
    else:
        print(A*B%m)
else:
    print(0)