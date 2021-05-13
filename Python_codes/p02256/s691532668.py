# GCD
def gcd(x, y):
    if x % y > 0:
        r = x % y
        d = gcd(y, r)
    else:
        d = y

    return d


x, y = [int(i) for i in input().split()]

if x < y:
    buff = x
    x = y
    y = buff
elif x == y:
    print(x)
    exit()

d = gcd(x, y)

print(d)