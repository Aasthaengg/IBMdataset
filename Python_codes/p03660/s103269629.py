N=int(input())
D=[[] for i in range(N)]
F,S=[-1]*N,[-1]*N
F[0]=0
S[N-1]=0
for i in range(N-1):
  a,b=map(int, input().split())
  a-=1
  b-=1
  D[a].append(b)
  D[b].append(a)
 
from collections import deque
import sys
sys.setrecursionlimit(10**7) 
dis=0

def bfs(n):
  t=0
  q=deque()
  q.append(n)
  while len(q):
    x=q.popleft()
    for i in D[x]:
      if F[i]==-1 and i!=x: 
        F[i]=F[x]+1
        q.append(i)

def bfs2(n):
  t=0
  q=deque()
  q.append(n)
  while len(q):
    x=q.popleft()
    for i in D[x]:
      if S[i]==-1 and i!=x:
        S[i]=S[x]+1
        q.append(i)
bfs(0)
bfs2(N-1)
f,s=0,0
for i in range(N):
  if F[i]<=S[i]:
    f+=1
  else:
    s+=1
#print(F,S,f,s)
if f<=s:
  print('Snuke')
else:
  print('Fennec')