from scipy.special import comb
N = int(input())
a = [input() for _ in range(N)]

d = dict()
for x in a:
  s = ''.join(sorted(x))
  if s not in d.keys():
    d[s] = 1
  else:
    d[s] += 1

print(sum([comb(i, 2, exact=True) for i in d.values()]))