(r,c) = tuple(map(int,input().split()))
graph = []
for i in range(r):
  lst = list(map(int,input().split()))
  lst.append(sum(lst))
  graph.append(lst)
lsf = []
for i in range(c + 1):
  s = 0
  for j in range(r):
    s += graph[j][i]
  lsf.append(s)
for l in graph:
  print(' '.join(map(str,l)))
print(' '.join(map(str,lsf)))


