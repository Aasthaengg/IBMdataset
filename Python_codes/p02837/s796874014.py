import itertools
n = int(input())
b = []
for i in range(n):
  a = int(input())
  c = []
  for j in range(a):
    x, y = map(int, input().split())
    c.append([x,y])
  b.append(c)
g = []
for i in list(itertools.product(range(2) ,repeat = n)):
  flag = True
  for j in range(n):
    if i[j] == 0:
      continue
    for x,y in b[j]:
      if i[x-1] != y:
        flag = False
        break
    if not flag:
      break
  if flag:
    g.append(sum(i))
print(max(g))