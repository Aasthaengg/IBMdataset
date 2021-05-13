import math
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

X = int(input())

while True:
  prime = int(math.sqrt(X))
  if is_prime(X):
    break
  X += 1
print(X)