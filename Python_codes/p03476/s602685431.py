import math


def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
    return data

primes = set(get_sieve_of_eratosthenes(10**5))
A = []
for i in range(1, 10**5+1):
  if i % 2 == 1:
    if i in primes and (i+1) // 2 in primes:
      A.append(1)
    else:
      A.append(0)
  else:
    A.append(0)

for i in range(1, len(A)):
  A[i] += A[i-1]

q = int(input())
for _ in range(q):
  l, r = map(int, input().split())
  if l == 1:
    l = 2
  ans = A[r-1] - A[l-2]
  print(ans)
