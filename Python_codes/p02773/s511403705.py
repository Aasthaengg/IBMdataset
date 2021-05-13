n = int(input())
d = {}
for _ in range(n):
  s = input()
  if s in d: d[s] += 1
  else: d[s] = 1
  
t = max(d.values())
for x,y in sorted(d.items()):
  if y == t: print(x)