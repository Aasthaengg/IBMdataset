N,M=map(int,input().split())
P=list(map(int,input().split()))
P=[i-1 for i in P]
par=[i for i in range(N)]
size=[1 for i in range(N)]
def find(x):
  if par[x]==x:
    return x
  else:
    par[x]=find(par[x])
    return par[x]
def union(a,b):
  x=find(a)
  y=find(b)
  if x!=y:
    if size[x]<size[y]:
      par[x]=par[y]
      size[y]+=size[x]
    else: 
      par[y]=par[x]
      size[x]+=size[y]
  else:
    return
for i in range(M):
  x,y=map(int,input().split())
  union(x-1,y-1)
count=0
for i in range(N):
  if find(i)==find(P[i]):
    count+=1
print(count)