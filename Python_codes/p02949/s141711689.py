n,m,p = map(int, input().split())
es = []
g1 = [[]for _ in range(n)]
g2 = [[] for _ in range(n)]
li = []
for i in range(m):
  a,b,c = map(int, input().split())
  li.append((a - 1,b - 1,c))
  g1[a - 1].append((b - 1,(c-p)*-1))
  g2[b - 1].append((a - 1,(c-p)*-1))
done1 = [0] * n
done1[0] = 1
s = [0]
while s:
  d = s.pop()
  for node,_ in g1[d]:
    if not done1[node]:
      done1[node] = 1
      s.append(node)
done2 = [0] * n
done2[n - 1] = 1
s = [n - 1]
while s:
  d = s.pop()
  for node, _ in g2[d]:
    if not done2[node]:
      done2[node] = 1
      s.append(node)
done = [0] * n
for i in range(n):
  done[i] = done1[i] & done2[i]
for a,b,c in li:
  if done[a] & done[b]:
    es.append((a,b,(c-p)*-1))
m = len(es)
d = [0]*n
for i in range(n):
  for j in range(m):
    f, t, c = es[j]
    if d[t] > d[f] + c:
      d[t] = d[f] + c
      if i == n - 1:
        print(-1)
        exit(0)
d = [float('inf')] * n
d[0] = 0
while(True):
  update = False
  for i in range(m):
    f, t, c = es[i]
    if d[f] != float('inf') and d[t] > d[f] + c:
      d[t] = d[f] + c
      update = True
  if not update:
    break
print(max(0, -d[n - 1]))
