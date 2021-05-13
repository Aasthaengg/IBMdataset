import math
a,b,c=map(int,input().split())

if (a+b-c)>=0:
    print("No")
else:
    if pow(c-a-b,2)>4*a*b:
        print("Yes")
    else:
        print("No")