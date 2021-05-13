x, y = map(int, input().split(' '))

def gcd(x1,x2):
    if(x2 == 0):
        return x1
    else:
        return gcd(x2, x1 % x2)
    
if(x>=y):
    print(gcd(x,y))
else:
    print(gcd(y,x))
