from collections import deque
n,q = map(int,input().split())
l = [[] for i in range(n+1)]
pts = [0]*(n+1)
for _ in range(n-1):
  a,b = map(int,input().split())
  l[a].append(b)
  l[b].append(a)
for _ in range(q):
  p,x = map(int,input().split())
  pts[p] += x
Q = deque()
Q.append(1)
ans = [0]*(n+1)
vst = [0]*(n+1)
while Q:
  temp = Q.popleft()
  for n in l[temp]:
    if vst[n]:
      continue
    ans[n] = ans[temp] + pts[temp]
    Q.append(n)
  ans[temp] += pts[temp]
  vst[temp] = 1
print(*ans[1:])