n,m = map(int,input().split())
pyl = [list(map(int,input().split())) for nesya in range(m)]
predic = dict()
ydic = dict()
spyl = sorted(pyl,key = lambda x:x[1])
for py in spyl:
  p = py[0]
  y = py[1]
  if p in predic:
    predic[p] += 1
  else:
    predic[p] = 1
  ydic[y] = (str(p).zfill(6))+(str(predic[p]).zfill(6))
for hoge in pyl:
  print(ydic[hoge[1]])