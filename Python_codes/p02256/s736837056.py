def gcd(x,y):
    r=x%y
    if r==0:
        return y
    else:
        return gcd(y,r)
x,y=map(int, input().split())
if x>y:
    r=gcd(x,y)
if x==y:
    r=x
if x<y:
    r=gcd(y,x);
print(r)

