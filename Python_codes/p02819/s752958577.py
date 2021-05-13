x = int(input())

import math
primes=[2]
def isPrime(n):
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  
  m = math.floor(math.sqrt(n))
  for p in primes:
      if n % p == 0:
        return False
      if p > m:
        break
  primes.append(n)
  return True

for i in range(2,x):
  isPrime(i)

n = x
while(True):
  if isPrime(n):
    print(n)
    exit(0)
  elif n > 10**6:
    exit(0)
  n += 1
