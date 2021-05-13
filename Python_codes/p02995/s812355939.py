A, B, C, D = map(int,input().split())

def gcd(x,y):
    if x<y:
        x, y = y, x
    r = x%y
    while r!=0:
        x = y
        y = r
        r = x%y
    return y

def lcm(x,y):
    return (x*y)//gcd(x,y)

L = lcm(C,D)

lenB = B-(B//C+B//D-B//L)
A-=1
lenA = A-(A//C+A//D-A//L)
print(lenB-lenA)