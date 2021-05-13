from collections import defaultdict
import math
prm = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
alp = {chr(i):p for i,p in zip(range(97, 97+26),prm)}
n = int(input())
d = defaultdict(int)
nums = set([])
for _ in range(n):
  s = input()
  m = 1
  for l in s:
    m *= alp[l]
  d[m] += 1

def comb(n, r):
  if n<r:
    return 0
  else:
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans = 0
for k in d.values():
  ans += comb(k,2)
print(ans)