from collections import deque

N, M = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(M)]
od = [-1]*(N+1)
low = [-1]*(N+1)
pa = [0]*(N+1)
od[1] = 0
low[1] = 0
pa[1] = 1
ni = {i:[] for i in range(1,N+1)}

for i in range(M):
  ni[edges[i][0]].append(edges[i][1])
  ni[edges[i][1]].append(edges[i][0])

rlt = 0
h = deque([])
for i in ni[1]:
  h.append([1,i])

i = 0
while h:
  a = h.pop()
  if od[a[1]] > -1:
    if od[a[1]] < od[a[0]]:
      low[a[0]] = od[a[1]]
      c = a[0]
      while low[pa[c]] > od[a[1]]:
        low[pa[c]] = od[a[1]]
        c = pa[c]
  else:
    i += 1
    od[a[1]] = i
    low[a[1]] = i
    pa[a[1]] = a[0]
    for b in ni[a[1]]:
      if b == a[0]:
        continue
      h.append([a[1],b])
          
for i in range(2,N+1):
  if od[pa[i]] < low[i]:
    rlt += 1

print(rlt)
