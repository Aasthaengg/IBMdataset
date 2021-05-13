from fractions import gcd
X,Y=map(int,input().split())
#n=X*Y/pow(gcd(X,Y),2)

if (X/Y).is_integer()==True:
    print("-1")
else:
    print(X)