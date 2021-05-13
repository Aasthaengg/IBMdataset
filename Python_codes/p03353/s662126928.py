import string
s = input()
k = int(input())
d=set()
for sp in string.ascii_lowercase:
  for i,sd in enumerate(s,start=0):
    if sp == sd:
      e=set()
      for l in range(1, 6):
        if i+l > len(s):
          break
        e.add(s[i:i+l])
      d=d|e
  if len(d) >= k:
    break

d=list(d)
d=sorted(d)
print(d[k-1])