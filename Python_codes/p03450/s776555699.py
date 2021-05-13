N,Q = map(int,input().split())
ABC = [list(map(int,input().split())) for i in range(Q)]
edge = [[] for _ in range(N)]

for a,b,c in ABC:
    edge[a-1].append([b-1,c])
    edge[b-1].append([a-1,-c])

numlist = [0] * N
MIN,MAX = 0,0
visited = [False] * N
ans = 0

for i in range(N):
    if visited[i]:
      continue
    stack = [i]
    visited[i] = True
    while stack:
      v = stack.pop()
      for u,d in edge[v]:
        if not visited[u]:
          numlist[u] = numlist[v] + d
          stack.append(u)
          visited[u] = True
ans = 0
for i in range(N):
    if numlist[i] < MIN: MIN = numlist[i]
    elif numlist[i] > MAX: MAX = numlist[i]
    for u,d in edge[i]:
      if numlist[i] + d != numlist[u]:
        ans = -1
        break
    else:
      continue
    break
if ans != -1:
    ans = 'Yes'
else:
  	ans = 'No'

    
print(ans)


