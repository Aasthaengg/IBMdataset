#閉路判定
#n=頂点数 e=隣接リスト
#flag=0...DAG判定　flag=1...トポロジカルソート
from collections import deque
def find_loop(n,e,flag):
  x=[0]*n
  d=deque()
  t=[]
  c=0
  for i in range(n):
    for j in edge[i]:x[j]+=1
  for i in range(n):
    if x[i]==0:
      d.append(i)
      t.append(i)
      c+=1
  while d:
    i=d.popleft()
    for j in edge[i]:
      x[j]-=1
      if x[j]==0:
        d.append(j)
        t.append(j)
        c+=1
  if flag==0:return c==n
  else:return t

n=int(input())
edge=[[]for _ in range(n*n)]
inp=[1]*n*n
p=lambda x,y:min(x,y)*n+max(x,y)
for i in range(n):
  a=list(map(int,input().split()))
  for j in range(1,n-1):
    edge[p(i,a[j-1]-1)].append(p(i,a[j]-1))
if find_loop(n*n,edge,0)==False:print(-1);exit()
t=find_loop(n*n,edge,1)
ans=[1]*n*n
for i in t:
  for j in edge[i]:ans[j]=max(ans[j],ans[i]+1)
print(max(ans))
