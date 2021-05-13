from collections import Counter
import math
def factorization(n):
    i = 2
    factors = []
    while i <= math.floor(math.sqrt(n)):
        if n%i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors
N = int(input())
if N==1:
    print(1)
    exit()
c = Counter()
for i in range(1, N+1):
    f = factorization(i)
    c.update(f)
ans = 1
for x in c.values():
    ans *= (x+1)
print(ans % int(1e9+7))