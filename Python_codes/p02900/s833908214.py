def make_divisors(n:int) -> list:
    """約数を列挙"""
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

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

A, B = map(int, input().split())
div_A = make_divisors(A)
div_B = make_divisors(B)
cd = (set(div_A) & set(div_B))
ans = 0
for n in cd:
    if isPrime(n):
        ans += 1
print(ans)