N, M = map(int, input().split())
mod = int(1e+9 + 7)
a = mod - 2
ax = []
while a != 0:
  ax = [a%2] + ax[:]
  a //= 2
def inved(x):
  y = 1
  for i in range(len(ax)):
    if ax[i] == 1:
      y *= x
      y %= mod
    if i != len(ax) - 1:
      y *= y
      y %= mod
  return y

p, n = 2, M
L = []
dig = 1
while n != 1:
  i = 0
  while n % p == 0:
    n //= p
    dig *= p
    i += 1
  if i != 0:
    L.append([p, i])
  p += 1
  if p > int(M**(1/2)) and dig != M:
    if L != []:
      L.append([M//dig, 1])
    else:
      L.append([M, 1])
    break

if M == 1:
  print(1)
else:
  prod = 1
  mm = max(x[1] for x in L)
  fact = [1]
  for i in range(N + mm - 1):
    fact.append((fact[i] * (i + 1)) % mod)
  invf = inved(fact[N - 1])
  for i in L:
    pad = (fact[N - 1 + i[1]] * inved(fact[i[1]]) * invf) % mod
    prod *= pad
    prod %= mod
  print(prod)