import math
m=int(input())

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
for i in range(m,m+1000):
  if is_prime(i):
    print(i)
    break