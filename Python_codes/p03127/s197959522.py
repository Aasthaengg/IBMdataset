from fractions import gcd


input()
A = map(int, input().split())
ans = next(A)
for a in A:
    ans = gcd(ans, a)
print(ans)
