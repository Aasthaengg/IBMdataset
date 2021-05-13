N = int(input())
ans = 0
import math
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
for i in make_divisors(N):
    tmp = (N - i) // i
    if tmp == 0:
        continue
    if N // tmp == N % tmp:
        ans += tmp
print(ans)