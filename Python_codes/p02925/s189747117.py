from collections import deque
def f(s,t):
  if s>t:
    a=s
    s=t
    t=a
  return n*(s-1)-s*(s-1)//2+t-s-1
n=int(input())
A=[list(map(int,input().split())) for i in range(n)]
E=[[] for i in range(n*(n-1)//2)]
EE=[[] for i in range(n*(n-1)//2)]
B=[0]*(n*(n-1)//2)
for i in range(n):
  for j in range(n-2):
    u=f(i+1,A[i][j])
    v=f(i+1,A[i][j+1])
    EE[u].append(v)
    E[v].append(u)
    B[v]+=1
D=deque([])
V=[0]*(n*(n-1)//2)
F=[10**9]*(n*(n-1)//2)
for i in range(n*(n-1)//2):
  if B[i]==0:
    D.append(i)
    V[i]=1
    F[i]=1
while len(D)>0:
  x=D[0]
  D.popleft()
  for i in range(len(EE[x])):
    B[EE[x][i]]-=1
    if B[EE[x][i]]==0:
      D.append(EE[x][i])
      F[EE[x][i]]=F[x]+1
      V[EE[x][i]]=1
ans=-1
for i in range(n*(n-1)//2):
  if F[i]>ans:
    ans=F[i]
if ans==10**9:
  print(-1)
else:
  print(ans)