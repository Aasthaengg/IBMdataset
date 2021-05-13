def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        g1 = gcd(a, b)
        if g1 == 1:
            ans += K
        else:
            for c in range(1, K+1):
                ans += gcd(g1, c)
print(ans)
