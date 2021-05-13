
from collections import Counter
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n //= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table

A,B = map(int,input().split())
p1 = Counter(prime_decomposition(A))
p2 = Counter(prime_decomposition(B))
ans = 1
for p,_ in p1.items():
  if p2[p] > 0:
    ans += 1

print(ans)