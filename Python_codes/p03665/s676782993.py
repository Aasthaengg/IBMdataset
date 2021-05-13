memo = [0] * 100
def f(x):
  global memo
  if x in [0, 1]:
    memo[x] = 1
    return 1
  else:
    if memo[x] > 0:
      return memo[x]
    else:
      memo[x] = x*f(x-1)
      return memo[x]

def comb(n, r):
  a = f(n)
  b = f(r)
  c = f(n-r)
  return a // b // c

N, P = map(int, input().split())
A = list(map(int, input().split()))
A = [a%2 for a in A]
n0 = A.count(0)
n1 = N - n0
base = 2 ** n0
m0 = m1 = 0
for i in range(n1+1):
  if i % 2:
    m1 += comb(n1, i)
  else:
    m0 += comb(n1, i)

if P == 0:
  print(base * m0)
else:
  print(base * m1)