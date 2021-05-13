def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
X = int(input())
a = gcd(360,X)
b = (X//a)*360
print(b//X)