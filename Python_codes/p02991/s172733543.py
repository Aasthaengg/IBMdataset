from collections import deque
N,M = map(int,input().split())
to = [[] for _ in range(N)]
for i in range(M):
  a,b = map(int,input().split())
  a-=1;b-=1
  to[a].append(b)
start,end = map(int,input().split())
start -= 1;end -= 1
#print(to)
INF = float("inf")
Q = deque([(start,0)]) #今の点、何歩目か
visit = [[INF,INF,INF] for _ in range(N)] #三歩目、一歩目、二歩目
visit[start][0] = 0
while Q: #今の点、けんけんぱのどれか、一個前に止まった点
  v,step = Q.popleft()
  now = visit[v][step]
  step = (step+1)%3 #ここでstep+1歩目でvへ行く
  for w in to[v]:
    #print(visit[w][step],step,now)
    if visit[w][step] != INF:
      continue
    Q.append((w,step)) #step歩目でwにいて次vへ行く。
    if step %3 == 0:
      visit[w][step] = min(visit[w][step],now+1)
    else:
      visit[w][step] = min(visit[w][step],now)
#print(visit)
if visit[end][0] == INF:
  ans = -1
else:
  ans = visit[end][0]
print(ans)