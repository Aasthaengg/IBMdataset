import math
from collections import Counter

n = int(input())
prime_count = Counter()
def prime_c(m):
  for i in range(2, math.ceil(math.sqrt(m))+1):
    while m % i == 0:
      m /= i
      prime_count[i] += 1
  if m > 1:
    prime_count[int(m)] += 1  

for i in range(2, n+1):
  prime_c(i)

mod = 10**9+7
ans = 1
for v in prime_count.values():
  ans *= (v+1) 
  ans %= mod 
print(ans)