def gcd(x,y):
    if y==0:
        return x
    if x<y:
        x,y=y,x
    x,y=y,x%y
    return gcd(x,y)
a,b=map(int,input().split())
print(a*b//gcd(a,b))