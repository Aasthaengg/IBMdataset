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
  #return is_prime
  return [i for i in range(n+1) if is_prime[i] and i%5 == 1]

ans = Sieve_of_Eratosthenes(55555)

print(*ans[:N])