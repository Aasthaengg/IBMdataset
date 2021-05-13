import math
N=int(input())

han=999999999999999999999999999999999999999999
b=0



for a in range(1,int(math.sqrt(N))+1):
    if N%a==0:
        A=N/a
        if A>a:
            gou=A-a
        else:
            gou=a-A
        b=a
        if gou<han:
            han=gou
            kot=A+a

print(int(kot)-2)
