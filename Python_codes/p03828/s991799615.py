
import math
from collections import Counter
from collections import defaultdict
mod = 10**9+7 

def prime(n):
  for i in range(2, math.ceil(math.sqrt(n))+1):
    while n % i == 0:
      n /= i
      prime_count[i] += 1
  if n > 1:
    prime_count[int(n)] += 1

n = int(input())
a = 1
prime_count = defaultdict(int)
for i in range(1, n+1):
  prime(i)

ans = 1
for v in prime_count.values():
  ans *= (v+1)
  ans %= mod 
print(ans)



