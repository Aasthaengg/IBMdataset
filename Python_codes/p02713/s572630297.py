K = int(input())
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        r = a % b
        return gcd(b, r)

ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            n = gcd(a, b)
            n = gcd(n, c)
            ans += n

print(ans)