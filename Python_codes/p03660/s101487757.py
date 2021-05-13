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
d_from_b=[-1]*n
d_from_w=[-1]*n
d_from_b[0]=0
todo=deque([0])
while todo:
  t=todo.popleft()
  l=ki[t]
  for li in l:
    if d_from_b[li]==-1:
      d_from_b[li]=d_from_b[t]+1
      todo.append(li)

d_from_w[n-1]=0
todo=deque([n-1])
while todo:
  t=todo.popleft()
  l=ki[t]
  for li in l:
    if d_from_w[li]==-1:
      d_from_w[li]=d_from_w[t]+1
      todo.append(li)
b_cnt=0
for i in range(n):
  if d_from_b[i]<=d_from_w[i]:
    b_cnt+=1
if n-b_cnt<b_cnt:
  print('Fennec')
else:
  print('Snuke')
#print(root)
#print(d_from_b,d_from_w)