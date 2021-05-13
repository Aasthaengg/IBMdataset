from collections import *
H,W=map(int,input().split())
S=[input() for i in range(H)]
INF=10**9
D=[[INF]*W for i in range(H)]
if S[0][0]=='.':
  D[0][0]=0
else:
  D[0][0]=1
Q=deque([(0,0)])
v=0
while len(Q):
  v=Q.popleft()
  if v[0]!=H-1:
    if S[v[0]][v[1]]=='.' and S[v[0]+1][v[1]]=='#':
      if D[v[0]][v[1]]+1<D[v[0]+1][v[1]]:
        D[v[0]+1][v[1]]=D[v[0]][v[1]]+1
        Q.append((v[0]+1,v[1]))
    else:
      if D[v[0]][v[1]]<D[v[0]+1][v[1]]:
        D[v[0]+1][v[1]]=D[v[0]][v[1]]
        Q.append((v[0]+1,v[1]))
  if v[1]!=W-1:
    if S[v[0]][v[1]]=='.' and S[v[0]][v[1]+1]=='#':
      if D[v[0]][v[1]]+1<D[v[0]][v[1]+1]:
        D[v[0]][v[1]+1]=D[v[0]][v[1]]+1
        Q.append((v[0],v[1]+1))
    else:
      if D[v[0]][v[1]]<D[v[0]][v[1]+1]:
        D[v[0]][v[1]+1]=D[v[0]][v[1]]
        Q.append((v[0],v[1]+1))
print(D[-1][-1])