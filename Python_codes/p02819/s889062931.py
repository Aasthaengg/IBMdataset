X = int(input())

def isPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  for p in range(2, n):
      if n % p == 0:
        return False
  return True

for i in range(X, 1000000):
    if isPrime(i) == True:
        print(i)
        exit()