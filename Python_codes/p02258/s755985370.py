n = int(input())
ps = [int(input()) for _ in range(n)]
maxpro = -999999999
minp = 1000000000
for i, p in enumerate(ps[:-1]):
  if p >= minp: continue
  pro = max(ps[i + 1:]) - p
  maxpro = max(pro, maxpro)
  minp = p
print(maxpro)