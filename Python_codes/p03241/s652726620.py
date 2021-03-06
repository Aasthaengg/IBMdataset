def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors
N,M = map(int,input().split())

d = M//N

divisor = sorted(make_divisors(M))

from bisect import *

b = bisect_left(divisor,d)
if divisor[b] == d:
  ans = divisor[b]
else:
  ans = divisor[b-1]
print(ans)