from fractions import gcd
n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for ai in a[1:]:
    ans = gcd(ans, ai)
print(ans)