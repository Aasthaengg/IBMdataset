def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
def lcm(a, b):
    return abs(a*b)//gcd(a, b)

n = int(input())
ans = int(input())
for i in range(1, n):
    t = int(input())
    ans = lcm(ans, t)
print (ans)