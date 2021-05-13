def gcd(a, b):
  if a > b:
    a, b = b, a
  while a % b != 0:
    a, b = b, a % b
  return b

n, k = map(int, input().split())
A = list(map(int, input().split()))
maxA = max(A)

l = A.pop()
for a in A:
  l = gcd(l, a)

print('POSSIBLE' if k % l == 0 and maxA >= k else 'IMPOSSIBLE')
