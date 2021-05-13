def gcd(a,b):
    if b==0:
        return a
    c=a%b
    return gcd(b,c)
x,y=map(int,input().split())
if x<y:
    x,y=y,x
m=gcd(x,y)
print(m)
