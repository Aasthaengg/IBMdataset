A, B, C = map(int, input().split())
import fractions
a = fractions.gcd(A, B)
ans = 'NO'
if a == 1:
  ans = 'YES'
elif C % a == 0:
  ans = 'YES'
print(ans)