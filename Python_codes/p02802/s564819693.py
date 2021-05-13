P,M = map(int,input().split())
dac = {}
dwa = {}
for _ in range(M):
  p,s = input().split()
  p = int(p)
  if s == "AC":
    if p not in dac:
      dac[p] = 1
  else:
    if p not in dac:
      if p not in dwa:
        dwa[p] = 1
      else:
        dwa[p] += 1

score = len(dac)
penalty = sum([val for k,val in dwa.items() if (k in dac)])
print(score,penalty)