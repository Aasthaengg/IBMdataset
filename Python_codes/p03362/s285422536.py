def is_prime(n):
  i = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += 1
  return True

N = int(input())

primes = []

for i in range(2,55556):
  if is_prime(i) == True:
    if i % 5 == 1:
      primes.append(i)
  if len(primes) == N:
    break

print(*primes)