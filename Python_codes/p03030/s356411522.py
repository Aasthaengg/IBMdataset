n = int(input())

m = {}
for i in range(n):
  s, p = input().split()
  p = int(p)
  if s not in m:
    m[s] = []
  
  m[s].append((p, i+1))

shops = sorted(m.items(), key=lambda x : x[0])

for x in shops:
  city, scores = x[0], sorted(x[1], reverse=True, key=lambda x : x[0])
  for score in scores:
    print(score[1])