from collections import deque
n=int(input())
G=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  a=a-1
  b=b-1
  G[a].append(b)
  G[b].append(a)
V=[0]*n
V[0]=1
P=[0]*n
P[0]=-1
C=[1]*n
D=deque([0])
DD=deque([0])
GG=[[] for i in range(n)]
while len(D)>0:
  v=D[0]
  D.popleft()
  for i in range(len(G[v])):
    if V[G[v][i]]==0:
      V[G[v][i]]=1
      D.append(G[v][i])
      DD.append(G[v][i])
      P[G[v][i]]=v
DD=list(DD)[::-1]
for i in range(n):
  if DD[i]!=0:
    C[P[DD[i]]]+=C[DD[i]]
a=0
i=n-1
while i!=0:
  i=P[i]
  a=a+1
i=n-1
for _ in range((a-1)//2):
  i=P[i]
s=C[i]
f=n-C[i]
if f>s:
  print("Fennec")
else:
  print("Snuke")