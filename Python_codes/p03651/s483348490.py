def gcd(a, b):
  if a < b:
    a, b = b, a
  while a % b:
    a, b = b, a % b
  return b

n, k = map(int, input().split())
a = list(map(int, input().split()))
a_gcd = a[0]
for i in range(n):
  a_gcd = gcd(a_gcd, a[i])
a_max = max(a)
if k <= a_max and k % a_gcd == 0:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')