from scipy.sparse.csgraph import dijkstra
n=int(input())
g=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)
d1=[-1]*n
d2=[-1]*n
q1=[0]
d1[0]=0
while q1:
  x=q1.pop()
  for t in g[x]:
    if d1[t]==-1:
      d1[t]=d1[x]+1
      q1.append(t)
q2=[n-1]
d2[n-1]=0
while q2:
  x=q2.pop()
  for t in g[x]:
    if d2[t]==-1:
      d2[t]=d2[x]+1
      q2.append(t)
cnt=0
for i in range(n):
  if d1[i]<=d2[i]:
    cnt+=1
if cnt>n//2:
  print('Fennec')
else:
  print('Snuke')