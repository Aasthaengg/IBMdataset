z = input().split()
x = int(z[0])
y = int(z[1])

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
print(gcd(x,y))