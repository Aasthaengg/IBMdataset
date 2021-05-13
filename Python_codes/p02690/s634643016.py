x = int(input())
d = {}
for i in range(1000):
  b = (-1000+i)**5
  d[b] = -1000+i
for i in range(1000):
  a = i**5
  d[a] = i
  if a-x in d:
    b = d[a-x]
    a = i
    break
print(a,b)