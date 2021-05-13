a, b = [int(i) for i in input().split()]

z = 0

def gcd(x,y):
    if x<y:
        z=x
        x=y
        y=z

    while x%y !=0:
        z=x%y
        x=y
        y=z
        gcd(x,y)
    return y

print(gcd(a,b))