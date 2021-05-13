K = int(input())

def gcd(a, b):
    if a == 0 or b == 0:
        return max(a,b)
    x, y = min(a,b), max(a,b)
    return gcd(x,y%x )

ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        x = gcd(a,b)
        for c in range(1, K+1):
            ans += gcd(x,c)
print(ans)
