def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
A,B,C,D = map(int,input().split())
a = gcd(C,D)
E = (C//a)*D
n1 = B//C
n2 = B//D
n3 = B//E
n = B-(n1+n2-n3)
m1 = (A-1)//C
m2 = (A-1)//D
m3 = (A-1)//E
m = A-1-(m1+m2-m3)
print(n-m)