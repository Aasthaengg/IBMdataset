import fractions
n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for x in a:
  ans = fractions.gcd(ans, x)
print(ans)