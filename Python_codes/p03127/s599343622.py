import fractions as frac
n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in a:
    ans = frac.gcd(ans, i)

print(ans)