from fractions import gcd

X,Y=map(int,input().split())

i=1

if X==Y or Y==1:
    print(-1)
    exit()

if Y//gcd(X,Y)==1:
    print(-1)
else:
    print((X*(Y//gcd(X,Y)-1)))
