def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def lcm(a, b):
    return a*b//gcd(a, b)

n = int(input())
t1 = int(input())
ans = t1
for _ in range(n-1):
    t2 = int(input())
    ans = lcm(ans, t2)
print(ans)
