A, B, C = map(int, input().split())
import fractions
g = fractions.gcd(A, B)
ans = 'NO'
if C % g == 0:
  ans = 'YES'
print(ans)