import itertools
n = int(input())
xy = []

for i in range(n):
  x,y = map(int, input().split())
  xy.append([x,y])


a,b = [],[]
for v in itertools.combinations(xy,2):
  z = list(v)
  z.sort()
  x = z[1][0]-z[0][0]
  y = z[1][1]-z[0][1]
  a.append([x,y])
  if [x,y] in b:
    continue
  b.append([x,y])

c = 0
for i in b:
  c = max(c,a.count(i))
print (n-c)