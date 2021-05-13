n = int(input())
d = {}
for _ in range(n):
  s = input()
  if s in d: d[s] += 1
  else: d[s] = 1
m = int(input())
for _ in range(m):
  t = input()
  if t in d: d[t] -= 1
  else: d[t] = -1
    
print(max(0, max(d.values())))