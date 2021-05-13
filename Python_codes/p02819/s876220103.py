from math import sqrt

def is_prime(n):
  max_factor = int(sqrt(n))
  for i in range(2, max_factor+1):
    if n % i == 0:
      return False
  return True

X=int(input())

for x in range(X, 10*X+1):
  if is_prime(x):
    print(x)
    break