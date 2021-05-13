def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

K = int(input())
ans = 0
for a in range(1, K+1):
    ans += a
    for b in range(1, a):
        g = gcd(a, b)
        ans +=  g * 6
        for c in range(1, b):
            ans += gcd(g, c) * 6
print(ans)
