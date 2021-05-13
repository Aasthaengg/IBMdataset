def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x // gcd(x, y) * y

X, Y = map(int, input().split())
L = lcm(X, Y)
res = L - X
if (L - X) % Y != 0 and (L - X) <= 10**18:
    print(L - X)
else:
    print(-1)