import math

def isPrime(n):
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  
  m = math.floor(math.sqrt(n)) + 1
  for p in range(3, m, 2):
    if n % p == 0:
      return False
  return True

N = int(input())
ans = []

for i in range(2,55556):
  if isPrime(i) and i%5 == 1:
    ans.append(i)
  if len(ans) == N:
    break

print(*ans)