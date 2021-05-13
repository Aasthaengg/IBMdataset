x,y=map(int,input().split())
if x<y:
    print(x)
    exit()

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

temp = gcd(x,y)

if y == temp:
    print(-1)
else:
    print(x)