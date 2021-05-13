from itertools import combinations
n = int(input())
d = {}
for _ in range(n):
  s = input()[0]
  if s in ["M","A","R","C","H"]:
    if s in d: d[s] += 1
    else: d[s] = 1

t = []
for k in d.keys(): t.append(k)
if len(t) < 3:
  print(0)
  exit()
  
ans = 0
for i in combinations(t, 3):
  ans += d[i[0]]*d[i[1]]*d[i[2]]
print(ans)