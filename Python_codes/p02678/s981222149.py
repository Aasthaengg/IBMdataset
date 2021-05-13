from collections import deque

n,m=map(int,input().split())
ab=[map(int,input().split()) for i in range(m)]

c=[[] for i in range(n+1)]

for a,b in ab:
  c[a].append(b)
  c[b].append(a)
seen = [float('inf')]*(n+1)
que=deque()
que.append(1)
seen[1] = 0
while que:
  s=que.popleft()
  for i in c[s]:
    if seen[i] == float('inf'):
      que.append(i)
      seen[i] = s
if sum(seen[2:]) == float('inf'):
  print('No')
else:
  print('Yes')
  for i in seen[2:]:
    print(i)