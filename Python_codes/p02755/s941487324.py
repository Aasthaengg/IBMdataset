import math
a,b=map(int,input().split())

A=math.ceil(a*12.5)
B=math.ceil(b*10)

x=math.floor(B*0.08)
y=math.floor(A*0.1)

if x==a and y==b :
    if A>B :
        print(B)
    else :
        print(A)

elif x==a :
    print(B)
elif y==b :
    print(A)
else :
    print(-1)