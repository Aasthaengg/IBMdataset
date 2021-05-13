from collections import Counter, defaultdict
from itertools import count
from functools import reduce


MOD = 10 ** 9 + 7
N = int(input())


def prime_factor(n):
  c = defaultdict(int)
  for i in count(2):
    if i * i > n:
      break
    while n % i == 0:
      c[i] += 1
      n //= i;
  if n != 1:
    c[n] = 1
  return Counter(c)

counter = reduce(
  lambda a, i: a + prime_factor(i),
  range(N, 1, -1),
  Counter()
)
  
answer = reduce(
  lambda a, c: (a * (c + 1)) % MOD,
  counter.values(),
  1
)

print(answer)