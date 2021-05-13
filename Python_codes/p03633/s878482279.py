def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
ans = 1
for i in range(n):
    t = int(input())
    ans *= t // gcd(ans, t)

print(ans)