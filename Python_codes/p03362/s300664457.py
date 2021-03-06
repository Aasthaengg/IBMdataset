N=int(input())
import math
def primes(x):
  if x < 2: return []
  primes = [i for i in range(x)]
  primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
  for prime in primes:
    if prime > math.sqrt(x): break
    if prime == 0: continue
    for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

  return [prime for prime in primes if prime != 0]

A=primes(55555)
B=[]
cnt=0
for i in A:
  if i%5==1:
    B.append(i)
    cnt+=1
    if cnt==N:
      print(*B)
      exit()