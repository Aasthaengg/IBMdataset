X = int(input())

def is_prime(n):
  for i in range(2, int(n ** 1/2) + 1):
    if n % i == 0:
      return False
  
  return True

for i in range(X, 100004):
  if is_prime(i):
    print(i)
    break