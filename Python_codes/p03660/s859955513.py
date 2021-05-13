n=int(input())
ki=[[] for _ in range(n)]
for _ in range(n-1):
  a,b=map(int,input().split())
  a-=1
  b-=1
  ki[a].append(b)
  ki[b].append(a)
# 0とn-1の最短ルートのうち0側に属するものn-1側に属するもの
from collections import deque
# seen[i]:0からの最短ルートでiの一つ前の頂点
seen=[-2]*n
seen[0]=-1
todo=deque([0])
while todo:
  t=todo.popleft()
  l=ki[t]
  for li in l:
    if seen[li]==-2:
      seen[li]=t
      todo.append(li)
      if li==n-1:
        break
root=[n-1]
now=n-1
while now!=0:
  root.append(seen[now])
  now=seen[now]
bend=root[(len(root)-2)//2+1]
wend=root[(len(root)-2)//2]
# 頂点数数え
seen=[0]*n
seen[bend]=1
seen[wend]=1
todo=[bend]
cnt=0
while todo:
  t=todo.pop()
  l=ki[t]
  cnt+=1
  for li in l:
    if seen[li]==0:
      todo.append(li)
      seen[li]=1
if n-cnt<cnt:
  print('Fennec')
else:
  print('Snuke')
#print(root)
#print(bend,wend)