from collections import deque
n,u,v=map(int,input().split())
u=u-1
v=v-1
G=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  a=a-1
  b=b-1
  G[a].append(b)
  G[b].append(a)
P=[0]*n #親のノード
P[v]=-1
F=[0]*n
D=deque([v])
V=[0]*n
V[v]=1
GG=[[] for i in range(n)]
while len(D)>0:
  x=D[0]
  D.popleft()
  for i in range(len(G[x])):
    if V[G[x][i]]==0:
      V[G[x][i]]=1
      D.append(G[x][i])
      P[G[x][i]]=x
      GG[x].append(G[x][i])
      F[G[x][i]]=F[x]+1
a=F[u]
ans1=(a-1)//2 #高橋君が上る回数
b=F[u]%2
if b==0:
  b=2 #上り切った後の差(1or2)
for i in range(ans1):
  u=P[u]
V=[0]*n
V[u]=1
V[P[u]]=1
F=[0]*n
D=deque([u])
while len(D)>0:
  x=D[0]
  D.popleft()
  for i in range(len(GG[x])):
    D.append(GG[x][i])
    F[GG[x][i]]=F[x]+1
ans2=max(F)
print(ans1+ans2+b//2)