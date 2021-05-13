import itertools
n = int(input())
xy = []
for i in range(n):
  x,y = map(int, input().split())
  xy.append([x,y])

a={}
for v in itertools.combinations(xy,2):
  z = list(v)
  z.sort()
  x = z[1][0]-z[0][0]
  y = z[1][1]-z[0][1]
  if (x,y) not in a:
    a[(x,y)] = 1
  else:
    a[(x,y)] += 1
if n == 1:
  print (1)
else:
  print (n-max(a.values()))