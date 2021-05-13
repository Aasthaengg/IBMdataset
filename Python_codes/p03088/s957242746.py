from collections import defaultdict
n = int(input())
cs = 'ATGC'
ng = [
  'AGC',
  'GAC',
  'ACG',
  'AGGC',
  'ATGC',
  'ACGC',
  'AGAC',
  'AGTC'
]

mod = 10**9 + 7
d = defaultdict(int)
for c1 in cs:
  for c2 in cs:
    for c3 in cs:
      s = c1 + c2 + c3
      if s not in ng:
        d[s] += 1
for i in range(3, n):
  nd = defaultdict(int)
  for key in d.keys():
    for c in cs:
      cn = key[1:3] + c
      cn4 = key + c
      if cn not in ng and cn4 not in ng:
        nd[cn] = (nd[cn] + d[key]) % mod
  d = nd
print(sum([d[key] for key in d]) % mod)
      
