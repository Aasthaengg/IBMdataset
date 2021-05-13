from fractions import gcd
from copy import deepcopy as dc
N, K = map(int, input().split())
A = list(map(int, input().split()))
def divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)
  divisors.sort()
  return divisors
div = divisors(sum(A))
def check(g):
  Atemp = dc(A)
  for i in range(N):
    Atemp[i] %= g
  Atemp.sort()
  i = len(A) - sum(Atemp) // g
  #print(g, i, max(sum(Atemp[: i]), len(Atemp[i: ]) * g - sum(Atemp[i: ])))
  if max(sum(Atemp[: i]), len(Atemp[i: ]) * g - sum(Atemp[i: ])) <= K:
    return True
  else:
    return False

res = 1
for d in div:
  if check(d) == True:
    res = d
print(res)