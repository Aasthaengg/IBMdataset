def fact(n):
  a = 1
  for i in range(2, n+1):
    a *= i
  return a

def comb(n, r):
  return fact(n) // fact(r) // fact(n-r)

n, p = map(int, input().split())
a = list(map(int, input().split()))

zero = 0
one = 0
for i in a:
  if i % 2 == 0:
    zero += 1
  else:
    one += 1

if p == 0:
  ans = 2 ** zero
  c = 0
  for i in range(0, one+1, 2):
    c += comb(one, i)
  ans *= c
  print(ans)
else:
  ans = 2 ** zero
  c = 0
  for i in range(1, one+1, 2):
    c += comb(one, i)
  ans *= c
  print(ans)