def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

n = int(input())
ans = 1
for _ in range(n):
    t = int(input())
    ans = lcm(ans, t)
print(ans)
