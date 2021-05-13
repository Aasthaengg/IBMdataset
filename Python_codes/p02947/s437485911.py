import math

def comb(n, r):
  if n < r:
    return 0
  else:
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
a = [input() for _ in range(N)]

d = dict()
for x in a:
  s = ''.join(sorted(x))
  if s not in d.keys():
    d[s] = 1
  else:
    d[s] += 1

print(sum([comb(i, 2) for i in d.values()]))