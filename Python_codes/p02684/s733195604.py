from collections import Counter
N, K = map(int,input().split())
tele = list(map(int, input().split()))

#A1から順にワープした時の経由順
now = 0
goal,loop,visit = [],[],[0]*N

while visit[now]!=2:

  if visit[now]==0:
    goal.append(now)
  else:
    loop.append(now)
    
  visit[now] += 1
  now = tele[now]-1

if len(goal)>K:
  print(goal[K]+1)
else:
  amari = len(goal)-len(loop)
  print(loop[(K-amari)%len(loop)]+1)