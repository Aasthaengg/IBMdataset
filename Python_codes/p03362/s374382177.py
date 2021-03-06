def sieve(n):
  ass = []
  is_prime = [True]*(n+1)
  is_prime[0] = False
  is_prime[1] = False

  for i in range(2, int(n**0.5)+1):
    if not is_prime[i]:
      continue
    for j in range(i*2, n+1, i):
      is_prime[j] = False
  for i in range(n+1):
    if is_prime[i]:
      ass.append(i)
  return(ass)

l = sieve(55600)
l = [i for i in l if i%5 ==1]
n = int(input())
#print(*l[0:n])
print(*l[0:n])