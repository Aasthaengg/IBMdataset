from collections import deque
n, q = map(int, input().split())
g = [[] for i in range(n)]
k = []
for i in range(n-1):
  a,b = map(int, input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)
for i in range(q):
  a,b = map(int, input().split())
  k.append([a-1,b])
m = [-1]*n
m[0] = 0
m1 = [-1]*n
m1[0] = 0
q = deque()
q.append(0)
while len(q):
  d = q.popleft()
  for i in g[d]:
    if m[i] == -1:
      m[i] = m[d]+1
    if m1[i] == -1:
      m1[i] = d
      q.append(i)
kyori = [[] for i in range(max(m)+1)]
for i,j in enumerate(m):
  kyori[j].append(i)
ans= [0]*n
for i,j in k:
  ans[i]+=j
for i in kyori[1:]:
  for j in i:
    ans[j] = ans[j] + ans[m1[j]]
print(' '.join(map(str,ans)))