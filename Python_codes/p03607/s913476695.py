n = int(input())
d = {}
for i in range(n):
  a = int(input())
  d[a] = d.get(a, 0) + 1

c = 0
for e in d.values():
  if e % 2 == 1:
    c += 1
print(c)