from collections import deque
N,M = map(int,input().split())
to = [[] for _ in range(N*3)]
for i in range(M):
  a,b = map(int,input().split())
  a-=1;b-=1
  to[a*3].append(b*3+1)
  to[a*3+1].append(b*3+2)
  to[a*3+2].append(b*3)
start,end = map(int,input().split())
start -= 1;end -= 1
#print(to)
INF = float("inf")
Q = deque([start*3])
visit = [INF for _ in range(N*3)]
visit[start*3] = 0
while Q:
  v = Q.popleft()
  for w in to[v]:
    if visit[w] != INF:
      continue
    visit[w] = visit[v]+1
    if w == end*3:
      print(visit[w]//3)
      exit()
    Q.append(w) #step歩目でwにいて次vへ行く。

#print(visit)
if visit[end*3] == INF:
  ans = -1
else:
  ans = visit[end*3]//3
print(ans)