N = int(input())

def Sieve_of_Eratosthenes(n):
  is_prime = [True] * (n+1)
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, int(n**0.5)+1):
    if not is_prime[i]:
      continue
    for j in range(i*2, n+1, i):
      is_prime[j] = False
  return is_prime
  #return [i for i in range(n+1) if is_prime[i]]

is_prime = Sieve_of_Eratosthenes(55555)
ans = []
i = 0

while N:
  if is_prime[1+5*i]:
    ans.append(1+5*i)
    N -= 1
  i += 1

print(*ans)