import sys
S=sys.stdin.readlines()
N,M=map(int,S[0].split())
G=[]
a,b,c=0,0,0
for i in range(M):
  a,b,c=map(int,S[i+1].split())
  G.append((a-1,b-1,-c))
INF=10**15
D=[INF]*N
D[0]=0
e=0
for i in range(N-1):
  for j in range(M):
    e=G[j]
    if D[e[0]]!=INF and D[e[1]]>D[e[0]]+e[2]:
      D[e[1]]=D[e[0]]+e[2]
X=D[N-1]
for j in range(M):
  e=G[j]
  if D[e[0]]!=INF and D[e[1]]>D[e[0]]+e[2]:
    D[e[1]]=D[e[0]]+e[2]
if X==D[N-1]:
  print(-X)
else:
  print('inf')