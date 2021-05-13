#from collections import Counter
n = int(input())
d = {}
for i in range(n):
  s = input()
  if s in d:
    d[s] += 1
  else:
    d[s] = 1

ds = sorted(d.items(), key=lambda t:(-t[1],t[0]))

m = ds[0][1]
#print(m)
ans = []
for k, v in ds:
  if v != m:
    break
  print(k)
