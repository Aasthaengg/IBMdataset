from collections import deque

N, M = map(int, input().split())
dic = {i:[] for i in range(1,N+1)}

for _ in range(M):
  l, r, d = map(int, input().split())
  dic[l].append((r,d))
  dic[r].append((l,-d))

memo = [0]*(N+1)
h = deque([])

for i in range(1,N+1):
  if memo[i] > 0:
    continue
  h.append((i,0))
  while h:
    t = h.popleft()
    for u in dic[t[0]]:
      if u[0] == t[1]:
        continue
      if memo[u[0]] == 0:
        memo[u[0]] = memo[t[0]] + u[1]
        h.append((u[0],t[0]))
      else:
        if memo[u[0]] - memo[t[0]] != u[1]:
          print('No')
          exit()
          
print('Yes')