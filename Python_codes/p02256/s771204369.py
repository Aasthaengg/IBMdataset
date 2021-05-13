x,y=map(int,input().split())

def gg(a,b):
    if a%b==0 and b%b==0:
        return b
    return gg(b,a%b)

if x>y:
    print(gg(x,y))
else:
    print(gg(y,x))

