N = int(input())

def factorize(n):
  b = 2
  fct = []
  while b * b <= n:
    while n % b == 0:
      n //= b
      fct.append(b)
    b = b + 1
  if n > 1:
    fct.append(n)
  return fct

prod = [0]*(N+1)
for i in range(2,N+1):
  for p in factorize(i):
    prod[p] += 1
ans = 1
#print(prod)
for i in range(2,N+1):
  ans *= prod[i]+1
  ans %= 10**9+7
print(ans)

#print(*ans, sep='\n')
