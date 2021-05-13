import fractions
N = int(input())
ans = int(input())
for i in range(1, N):
  b = int(input())
  ans = ans*b//fractions.gcd(ans, b)
print(ans)