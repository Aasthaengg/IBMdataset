from collections import deque
N = int(input())
G = [[] for i in range(N+1)]
for i in range(N-1):
  a,b = map(int,input().split())
  G[a].append(b)
  G[b].append(a)
c = list(map(int,input().split()))
c.sort()
M = sum(c)-c[-1]

score = [0 for i in range(N+1)]

seen = [False for i in range(N+1)]
seen[1] = True
score[1] = c.pop()
d = deque([1])
while len(d)>0:
  v = d.pop()
  for i in G[v]:
    if seen[i] == False:
      seen[i] = True
      score[i] = c.pop()
      d.append(i)
###
print(M)
print(*score[1:])