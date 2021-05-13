def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a

K = int(input())
ans = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    ab = gcd(a,b)
    for c in range(1, K+1):
      ans += gcd(ab,c)

print(ans)