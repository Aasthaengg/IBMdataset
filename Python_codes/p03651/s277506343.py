def gcd(a, b):
  if a > b:
    a, b = b, a
  while a % b != 0:
    a, b = b, a % b
  return b

n, k = map(int, input().split())
A = list(map(int, input().split()))

g = A[0]
for i in range(1, n):
  g = gcd(g, A[i])

if k in A or max(A) > k and k % g == 0:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')