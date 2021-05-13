def get_primes(n):
  if n<=1:
    return []
  prime=[2]
  limit=int(n**0.5)
  p=[i+1 for i in range(2,n,2)]
  while limit>p[0]:
    prime.append(p[0])
    p=[j for j in p if j%p[0]!=0]
  return prime+p

N = int(input())

ans = []
primes = get_primes(55555)
for i in range(3, 55555 + 1, 2):
  if i in primes and i%5 == 1:
    ans.append(i)
  if len(ans) == N:
    break
print(*ans)