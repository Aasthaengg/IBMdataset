def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)

while True:
    try:
        x,y=map(int,input().split())
    except:
        break
    print(gcd(x,y),x*y//gcd(x,y))