n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

c, d, e = [],[],[]

for i in range(n):
  if p[i] <= a:
    c.append(p[i])
  elif p[i] <= b:
    d.append(p[i])
  else:
    e.append(p[i])
print (min(len(c),len(d),len(e)))