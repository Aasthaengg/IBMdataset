import sys
from math import sqrt
input = sys.stdin.readline
N = int(input())
sq = sqrt(N)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
#print(make_divisors(N))
res = 0
div = make_divisors(N)
for i in range(len(div)):
  if div[i] - 1 > sq: res += div[i] - 1
print(res)