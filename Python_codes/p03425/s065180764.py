from collections import defaultdict
from itertools import groupby, accumulate, product, permutations, combinations
def solve():
  d = defaultdict(lambda: 0)
  N = int(input())
  for i in range(N):
    S = input()
    d[S[0]] += 1
  s = 'MARCH'
  s = list(s)
  cnt = 0
  for com in combinations(s,3):
    prod = 1
    for c in com:
      prod *= d[c]
    cnt += prod
  return cnt
print(solve())