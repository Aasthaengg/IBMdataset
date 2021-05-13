def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
A,B,C,D = map(int,input().split())
c1 = B//C-(A-1)//C
d1 = B//D-(A-1)//D
E = (C//gcd(C,D))*D
e1 = B//E-(A-1)//E
print(B-A+1-c1-d1+e1)